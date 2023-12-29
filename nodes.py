import re

class DimensionProviderRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dimension": (["Portrait 832x1216", "Square 1024x1024", "Landscape 1216x832",  "Portrait 1024x1536", "Square 1472x1472", "Landscape 1536x1024"],),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("ratio_width", "ratio_height")
    FUNCTION = "provide_dimensions"
    OUTPUT_NODE = True
    CATEGORY = "DimensionProviderRatio"

    def provide_dimensions(self, dimension):
        dims = ["832x1216", "1024x1024", "1216x832", "1024x1536", "1472x1472", "1536x1024"]
        pattern = "[^0-9x]"
        cleaned_dimension = re.sub(pattern, "", dimension)
        index = dims.index(cleaned_dimension)
        img_dims = cleaned_dimension.split("x")
        return int(img_dims[0]), int(img_dims[1])

class DimensionProviderFree:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 1, "max": 10000}),
                "height": ("INT", {"default": 768, "min": 1, "max": 10000})
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("free_width", "free_height")
    FUNCTION = "provide_dimensions"
    OUTPUT_NODE = True
    CATEGORY = "DimensionProviderFree"

    def provide_dimensions(self, width, height):
        return (width, height)

class StringConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string_1": ("STRING", {"default": "", "multiline": False}),
                "string_2": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "concat_string"
    OUTPUT_NODE = True
    CATEGORY = "concat_string"

    def concat_string(self, string_1, string_2):
        return (f'{string_1}, {string_2}',)


NODE_CLASS_MAPPINGS = {
    "DimensionProviderRatio modusCell": DimensionProviderRatio,
    "DimensionProviderFree modusCell": DimensionProviderFree,
    "String Concat modusCell": StringConcat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Ratio": "Width and Height Node",
    "Free": "Width and Height Node"
}
