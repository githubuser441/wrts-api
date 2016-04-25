class Boeken(object):
    def __init__(self, wrts):
        self.wrts = wrts

    def convert_raw(wrts, raw):
        obj = Boeken(wrts)
        obj.id = raw["id"]
        obj.description = raw["description"]
        obj.title = raw["title"]

        obj.methods = raw["methods"]
        obj.methods_id = [a["id"] for a in raw["methods"]]
        obj.methods_name = [a["name"] for a in raw["methods"]]
        obj.methods_description = [a["description"] for a in raw["methods"]]
        obj.methods_subject = [a["subject"] for a in raw["methods"]]
        obj.methods_publisher_id = [a["publisher_id"] for a in raw["methods"]]
        obj.methods_slug = [a["slug"] for a in raw["methods"]]
        obj.methods_created_at = [a["created_at"] for a in raw["methods"]]
        obj.methods_updated_at = [a["updated_at"] for a in raw["methods"]]
        obj.methods_school_subject_id = [a["school_subject_id"] for a in raw["methods"]]
        obj.methods_is_old_method = [a["is_old_method"] for a in raw["methods"]]
        obj.methods_visible = [a["visible"] for a in raw["methods"]]

        obj.lists = raw["lists"]
        obj.lists_id = [a["id"] for a in raw["lists"]]
        obj.lists_user_id = [a["user_id"] for a in raw["lists"]]
        obj.lists_title = [a["title"] for a in raw["lists"]]
        obj.lists_created_at = [a["created_at"] for a in raw["lists"]]
        obj.lists_updated_at = [a["updated_at"] for a in raw["lists"]]
        obj.lists_shared = [a["shared"] for a in raw["lists"]]

        obj.lists_list_collection = [a["list_collection"] for a in raw["lists"]]
        #obj.lists_list_collection_lists = [w["lists"] for w in [a["list_collection"] for a in raw["lists"]]]
        # TODO: specifieker filteren

        return obj
