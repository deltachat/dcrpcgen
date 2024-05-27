"""Utilities for Java code generation."""

from __future__ import annotations

from typing import Any


def get_banner() -> str:
    """Get common banner comment to be added at the start of generated files"""
    return "/* Autogenerated file, do not edit manually */"


def create_comment(text: str, indentation: str = "") -> str:
    """Generate a Java comment"""
    if "\n" not in text:
        return f"{indentation}/* {text.strip()} */\n"

    comment = f"{indentation}/**\n"
    for line in text.split("\n"):
        if line.strip():
            comment += f"{indentation} * {line}\n"
        else:
            comment += f"{indentation} *\n"
    return comment + f"{indentation} */\n"


def decode_type(property_desc: dict[str, Any]) -> tuple[str, bool]:
    """Decode a type, it can be a returning type or parameter type"""
    if "anyOf" in property_desc:
        assert len(property_desc["anyOf"]) == 2
        assert property_desc["anyOf"][1] == {"type": "null"}
        ref = property_desc["anyOf"][0]["$ref"]
        assert ref.startswith("#/components/schemas/")
        typ = ref.removeprefix("#/components/schemas/")
        return typ, True

    if "$ref" in property_desc:
        assert property_desc["$ref"].startswith("#/components/schemas/")
        typ = property_desc["$ref"].removeprefix("#/components/schemas/")
        return typ, False

    if property_desc["type"] == "null":
        return "void", False  # only for function returning type

    if "null" in property_desc["type"]:
        assert len(property_desc["type"]) == 2
        assert property_desc["type"][1] == "null"
        property_desc["type"] = property_desc["type"][0]
        if typ := decode_type(property_desc)[0]:
            return typ, True
    elif property_desc["type"] == "boolean":
        return "Boolean", False
    elif property_desc["type"] == "integer":
        return "Integer", False
    elif property_desc["type"] == "number" and property_desc["format"] == "double":
        return "Float", False
    elif property_desc["type"] == "string":
        return "String", False
    elif property_desc["type"] == "array":
        if isinstance(property_desc["items"], list):
            count = len(property_desc["items"])
            if count == 2:
                typ1 = decode_type(property_desc["items"][0])[0]
                typ2 = decode_type(property_desc["items"][1])[0]
                return f"Pair<{typ1}, {typ2}>", False
            raise ValueError(
                f"Tuple not implemented for {count} elements: {property_desc}"
            )
        items_type = decode_type(property_desc["items"])[0]
        return f"java.util.List<{items_type}>", False
    elif "additionalProperties" in property_desc:
        additional_properties = property_desc["additionalProperties"]
        return f"java.util.Map<String, {decode_type(additional_properties)[0]}>", False
    raise ValueError(f"Not supported: {property_desc!r}")
