import requests

class OutlookParser:
    def __init__(self, headers, params, base):
        self.headers = headers
        self.params = params
        self.base = base

    def getvalue(self):
        return requests.get(self.base, headers = self.headers, params = self.params).json()['value']

    def getnext(self):
        if self.params == None:
            return requests.get(self.base, headers = self.headers).json()['@odata.nextLink']
        else:
            return requests.get(self.base, headers = self.headers, params = self.params).json()['@odata.nextLink']

    def changeheaders(self, newHeader):
        self.headers = newHeader

    def changeparams(self, newParams):
        self.params = newParams

class Queue():
    def __init__(self):
        self.items = []

    def getsize(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()