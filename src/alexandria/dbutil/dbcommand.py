# Author: Olin Gallet
# Date: 25/1/2023
#
# The WebsiteInterface is to be implemented by all potential websites
# that would be crawled.  It provides an abstract function for scraping the website.

from abc import ABC, abstractmethod

class DBCommand(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, cursor):
        pass

    