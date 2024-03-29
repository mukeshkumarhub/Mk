import os


class ComfyUI_IPAdapter_plus:
    @staticmethod
    def prepare():
        # create the ipadapter folder in ComfyUI/models/ipadapter
        # if it doesn't exist at setup time then the plugin defers to the base directory
        # and won't look for our ipadaters that are downloaded on demand
        if not os.path.exists("ComfyUI/models/ipadapter"):
            os.makedirs("ComfyUI/models/ipadapter")
