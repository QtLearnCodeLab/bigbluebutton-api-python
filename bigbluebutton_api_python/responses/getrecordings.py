from .base import BaseResponse
from ..core.record import Record
import jxmlease


class GetRecordingsResponse(BaseResponse):

    def get_recordings(self):
        obj = self.get("xml")
        recordings = []
        
        try:
            if obj.get('messageKey') == "noRecordings":
                return []
        except KeyError:
            pass
        recording = obj.get("recordings")
        recording = recording.get("recording")

        if isinstance(recording, jxmlease.dictnode.XMLDictNode) :
            recordings.append(Record(recording))
        
        if isinstance(recording, jxmlease.listnode.XMLListNode) :

            for recordXml in recording:
                recordings.append(Record(recordXml))

        return recordings
