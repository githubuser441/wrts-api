class Uitgevers(object):
    def __init__(self, wrts):
        self.wrts = wrts

    def convert_raw(wrts, raw):
        obj = Uitgevers(wrts)
        obj.id = raw["id"]
        obj.name = raw["name"]
        obj.logo_url = raw["logo_url"]
        obj.slug = raw["slug"]
        obj.description = raw["description"]

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

        obj.user_email = raw["user_email"]
        obj.user_full_name = raw["user_full_name"]
        obj.user_phone_number = raw["user_phone_number"]
        obj.user_last_sign_in = raw["user_last_sign_in"]
        obj.user_id = raw["user_id"]
        obj.ga_event = raw["ga_event"]
        obj.visible = raw["visible"]

        return obj
