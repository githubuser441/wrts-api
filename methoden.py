class Methoden(object):
    def __init__(self, wrts):
        self.wrts = wrts

    def convert_raw(wrts, raw):
        obj = Methoden(wrts)
        obj.id = raw["id"]
        obj.slug = raw["slug"]
        obj.name = raw["name"]
        obj.description = raw["description"]
        obj.subject = raw["subject"]

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

        obj.covers = raw["covers"]
        obj.covers_id = [a["id"] for a in raw["covers"]]
        obj.covers_image_file_name = [a["image_file_name"] for a in raw["covers"]]
        obj.covers_composed_title = [a["composed_title"] for a in raw["covers"]]
        obj.covers_edition_name = [a["edition_name"] for a in raw["covers"]]

        obj.publisher = raw["publisher"]
        obj.publisher_id = raw["publisher"]["id"]
        obj.publisher_user_id = raw["publisher"]["user_id"]
        obj.publisher_name = raw["publisher"]["name"]
        obj.publisher_description = raw["publisher"]["description"]
        obj.publisher_slug = raw["publisher"]["slug"]
        obj.publisher_created_at = raw["publisher"]["created_at"]
        obj.publisher_updated_at = raw["publisher"]["updated_at"]
        obj.publisher_logo = raw["publisher"]["logo"]
        obj.publisher_ga_event = raw["publisher"]["ga_event"]
        obj.publisher_visible = raw["publisher"]["visible"]

        obj.school_subject_id = raw["school_subject_id"]
        obj.is_old_method = raw["is_old_method"]
        return obj
