from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):

    def hook(self, context: dict) -> dict:
        """Add hook to update context based on user's input."""
        if context["plugin_type"] == "Model":
            if context["plugin_model_type"] == "Detector":
                context = self._chose_detector(context)
            else: # motor model
                context = self._chose_motor(context)
        return context
    
    def _chose_detector(self, context: dict) -> dict:
        """Select which detector model base class to use."""
        if context["mm_support"]:
            context["plugin_base"] == "ExEngineMMCameraModel"
        else:
            context["plugin_base"] == "ExEngineDetectorModel"
        return context
    
    def _chose_motor(self, context: dict) -> dict:
        """Select which motor model base class to use."""
        if context["plugin_motor_type"] == "Single":
            if context["mm_support"]:
                context["plugin_base"] == "ExEngineMMSingleMotorModel"
            else:
                context["plugin_base"] == "ExEngineSingleMotorModel"
        else: # dual-axis (XY) motor
            if context["mm_support"]:
                context["plugin_base"] == "ExEngineMMDoubleMotorModel"
            else:
                context["plugin_base"] == "ExEngineDoubleMotorModel"
        return context
    