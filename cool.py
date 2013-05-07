import sublime, sublime_plugin, shutil, re

project = 'cool-common'

class CoolListener(sublime_plugin.EventListener):
  def on_post_save(self, view):
    path = view.file_name()
    if (project in path):
        dest = re.sub(r'^(.*' + project + ').*(META\-INF.*)$', r'\1\\target\\classes\\\2', path)
        shutil.copy2(path, dest)
