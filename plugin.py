from pathlib import Path

from LSP.plugin import LspPlugin, OnPreStartContext
from lsp_utils import NodeManager
from sublime_lib import ResourcePath
from typing_extensions import override


def plugin_loaded():
	LspAureliaPlugin.register()


def plugin_unloaded():
	LspAureliaPlugin.unregister()


class LspAureliaPlugin(LspPlugin):

	@classmethod
	@override
	def on_pre_start_async(cls, context: OnPreStartContext) -> None:
		package_name = cls.plugin_storage_path.name
		NodeManager.on_pre_start_async(
			context,
			cls.plugin_storage_path,
			ResourcePath("Packages", package_name, "server-local"),
			Path("out", "server.js"),
			node_version_requirement=">=18",
		)
