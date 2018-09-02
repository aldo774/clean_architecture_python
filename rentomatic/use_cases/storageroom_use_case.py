from rentomatic.shared import response_object as res


class StorageRoomListUseCase(object):

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object):
        storage_rooms = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(storage_rooms)
