'''
Sublime Text plugin to allow resource hot-reloading, useful with tomcat-maven-plugin

it will copy to target/classes/META-INF/$PATH each time
 a resource src/main/resources/META-INF/$PATH is saved

e.g. cp src/main/resources/META-INF/js/script.js target/classes/META-INF/js/script.js

'''

import os
import re
import shutil
import sublime_plugin

RESOURCES_PATH = 'src/main/resources/META-INF'

class ReloadListener(sublime_plugin.EventListener):
    '''
    listener class
    '''
    def on_post_save(self, view):
        '''
        on_post_save listener action
        '''
        path = view.file_name()
        if RESOURCES_PATH in path:
            grps = re.match(r'^(.*)' + os.path.sep + RESOURCES_PATH + os.path.sep + '(.*)$', path)
            dest = os.path.join(grps.group(1), 'target', 'classes', 'META-INF', grps.group(2))
            shutil.copy2(path, dest)
