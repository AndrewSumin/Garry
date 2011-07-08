import frontik
import frontik.handler
import json
import garry.config

class PageHandler(frontik.handler.PageHandler):
	Dict = {}
	Dict["config"] = dict(static_host = garry.config.static_host)
	
	def set_template(self, name):
		self.template = self.config.templates.get_template(name)

	def _finish_page(self):
		if not self._finished:
			self.log.stage_tag("page")

			self.finish(self.template.render(self.Dict))
		else:
			self.log.warn('trying to finish already finished page, probably bug in a workflow, ignoring')	
