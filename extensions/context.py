from copier_templates_extensions import ContextHook    

class ContextUpdater(ContextHook):

    # TODO: add entry point context for controllers
    def hook(self, context: dict) -> dict:
        """Add hook to update context based on user's input."""
        if context["plugin_type"] == "Controller":
            context["module_import"] = "controller"
            context["plugin_base"] = "BlueskyController"
            context["registry"] = "DeviceRegistry"
            context["class_baseline"] = "MyController"
        else:
            context = self._chose_bluesky_context(context)        
        context = self._set_config_info(context)
        context["plugin_engine"] = "bluesky"
        return context
    
    def _set_config_info(self, context: dict) -> dict:
        """Set config_info and config_base based on plugin_type."""
        if context["plugin_type"] == "Model":
            if context["plugin_model_type"] == "Detector":
                context["config_base"] = "DetectorModelInfo"
            else: # motor model
                context["config_base"] = "MotorModelInfo"
        context["config_info"] = context["class_baseline"] + "Info"
        return context

    def _chose_bluesky_context(self, context: dict) -> dict:
        """Select which Bluesky model base class to use."""
        if context["plugin_type"] == "Model":
            context["module_import"] = "model"
            if context["plugin_model_type"] == "Detector":
                context["plugin_base"] = "DetectorModel"
                context["entry_point_group"] = "redsun.plugins.detectors"
            else: # motor model
                context["plugin_base"] = "MotorModel"
                context["entry_point_group"] = "redsun.plugins.motors"
        context["entry_point_value"] = context["class_baseline"].lower()
        context["entry_point_cfg_value"] = context["class_baseline"].lower() + "_config"
        return context
    
    