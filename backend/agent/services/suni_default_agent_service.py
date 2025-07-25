from typing import Dict, Any, Optional
from utils.logger import logger
from services.supabase import DBConnection
from agent.suni import SuniSyncService


class SuniDefaultAgentService:
    def __init__(self, db: DBConnection = None):
        self._sync_service = SuniSyncService()
        self._db = db or DBConnection()
        logger.info("🔄 SuniDefaultAgentService initialized with modular backend")
    
    async def get_suni_default_config(self) -> Dict[str, Any]:
        current_config = self._sync_service.config_manager.get_current_config()
        return current_config.to_dict()
    
    async def sync_all_suni_agents(self) -> Dict[str, Any]:
        logger.info("🔄 Delegating to modular sync service (preserves user customizations)")
        result = await self._sync_service.sync_all_agents()
        
        return {
            "updated_count": result.synced_count,
            "failed_count": result.failed_count,
            "details": result.details
        }
    
    async def update_all_suni_agents(self, target_version: Optional[str] = None) -> Dict[str, Any]:
        logger.info("🔄 Delegating to modular sync service (version auto-detected)")
        return await self.sync_all_suni_agents()
    
    async def install_for_all_users(self) -> Dict[str, Any]:
        logger.info("🔄 Delegating to modular installation service")
        result = await self._sync_service.install_for_all_missing_users()
        
        return {
            "installed_count": result.synced_count,
            "failed_count": result.failed_count,
            "details": result.details
        }
    
    async def install_suni_agent_for_user(self, account_id: str, replace_existing: bool = False) -> Optional[str]:
        logger.info(f"🔄 Installing Suni agent for user: {account_id}")
        
        try:
            if replace_existing:
                agents = await self._sync_service.repository.find_all_suni_agents()
                existing = next((a for a in agents if a.account_id == account_id), None)
                if existing:
                    await self._sync_service.repository.delete_agent(existing.agent_id)
                    logger.info(f"Deleted existing Suni agent for replacement")
            else:
                agents = await self._sync_service.repository.find_all_suni_agents()
                existing = next((a for a in agents if a.account_id == account_id), None)
                if existing:
                    logger.info(f"User {account_id} already has Suni agent: {existing.agent_id}")
                    return existing.agent_id

            current_config = self._sync_service.config_manager.get_current_config()
            agent_id = await self._sync_service.repository.create_suni_agent_simple(
                account_id,
                current_config.version_tag
            )
            
            logger.info(f"Successfully installed Suni agent {agent_id} for user {account_id}")
            return agent_id
                
        except Exception as e:
            logger.error(f"Error in install_suni_agent_for_user: {e}")
            return None
    
    async def get_suni_agent_stats(self) -> Dict[str, Any]:
        logger.info("🔄 Delegating stats to modular service")
        return await self._sync_service.get_sync_status() 