"""Tests for the stdio entry point."""
import pytest

from planka_mcp import stdio


class TestStdioEntryPoint:
    """Test the MCP tools registered by the stdio entry point."""

    @pytest.mark.asyncio
    async def test_registers_all_tools(self):
        """Test that every Planka tool is exposed."""
        tools = await stdio.mcp.list_tools()

        assert {tool.name for tool in tools} == {
            "planka_get_workspace",
            "planka_list_cards",
            "planka_find_and_get_card",
            "planka_get_card",
            "planka_create_card",
            "planka_update_card",
            "planka_delete_card",
            "planka_add_task",
            "planka_update_task",
            "planka_add_card_label",
            "planka_remove_card_label",
            "planka_delete_task",
        }
