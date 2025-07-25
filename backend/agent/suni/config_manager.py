import datetime
from typing import Dict, Any
from dataclasses import dataclass
from agent.suni.config import SuniConfig


@dataclass
class SuniConfiguration:
    name: str
    description: str
    configured_mcps: list
    custom_mcps: list
    restrictions: Dict[str, Any]
    version_tag: str


class SuniConfigManager:
    def get_current_config(self) -> SuniConfiguration:
        version_tag = self._generate_version_tag()
        
        return SuniConfiguration(
            name=SuniConfig.NAME,
            description=SuniConfig.DESCRIPTION,
            configured_mcps=SuniConfig.DEFAULT_MCPS.copy(),
            custom_mcps=SuniConfig.DEFAULT_CUSTOM_MCPS.copy(),
            restrictions=SuniConfig.USER_RESTRICTIONS.copy(),
            version_tag=version_tag
        )
    
    def has_config_changed(self, last_version_tag: str) -> bool:
        current = self.get_current_config()
        return current.version_tag != last_version_tag
    
    def validate_config(self, config: SuniConfiguration) -> tuple[bool, list[str]]:
        errors = []
        
        if not config.name.strip():
            errors.append("Name cannot be empty")
            
        return len(errors) == 0, errors
    
    def _generate_version_tag(self) -> str:
        import hashlib
        import json
        
        config_data = {
            "name": SuniConfig.NAME,
            "description": SuniConfig.DESCRIPTION,
            "system_prompt": SuniConfig.get_system_prompt(),
            "default_tools": SuniConfig.DEFAULT_TOOLS,
            "avatar": SuniConfig.AVATAR,
            "avatar_color": SuniConfig.AVATAR_COLOR,
            "restrictions": SuniConfig.USER_RESTRICTIONS
        }
        
        config_str = json.dumps(config_data, sort_keys=True)
        hash_obj = hashlib.md5(config_str.encode())
        return f"config-{hash_obj.hexdigest()[:8]}" 