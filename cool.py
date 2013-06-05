import sublime, sublime_plugin, shutil, re, os

project = 'cool-common'

class CoolListener(sublime_plugin.EventListener):
  def on_post_save(self, view):
    path = view.file_name()
    if (project in path):
        grps = re.match(r'^(.*' + project + ').*(META\-INF.*)$', path)
        dest = os.path.join(grps.group(1), 'target', 'classes', grps.group(2))
        shutil.copy2(path, dest)