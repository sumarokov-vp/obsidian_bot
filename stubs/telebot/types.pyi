from _typeshed import Incomplete
from abc import ABC
from telebot import service_utils as service_utils
from typing import Dict, List, Optional, Union

DISABLE_KEYLEN_ERROR: bool
logger: Incomplete

class JsonSerializable:
    def to_json(self) -> None: ...

class Dictionaryable:
    def to_dict(self) -> None: ...

class JsonDeserializable:
    @classmethod
    def de_json(cls, json_string) -> None: ...
    @staticmethod
    def check_json(json_type, dict_copy: bool = ...): ...

class Update(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    update_id: Incomplete
    message: Incomplete
    edited_message: Incomplete
    channel_post: Incomplete
    edited_channel_post: Incomplete
    inline_query: Incomplete
    chosen_inline_result: Incomplete
    callback_query: Incomplete
    shipping_query: Incomplete
    pre_checkout_query: Incomplete
    poll: Incomplete
    poll_answer: Incomplete
    my_chat_member: Incomplete
    chat_member: Incomplete
    chat_join_request: Incomplete
    def __init__(self, update_id, message, edited_message, channel_post, edited_channel_post, inline_query, chosen_inline_result, callback_query, shipping_query, pre_checkout_query, poll, poll_answer, my_chat_member, chat_member, chat_join_request) -> None: ...

class ChatMemberUpdated(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    chat: Incomplete
    from_user: Incomplete
    date: Incomplete
    old_chat_member: Incomplete
    new_chat_member: Incomplete
    invite_link: Incomplete
    via_chat_folder_invite_link: Incomplete
    def __init__(self, chat, from_user, date, old_chat_member, new_chat_member, invite_link: Incomplete | None = ..., via_chat_folder_invite_link: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def difference(self) -> Dict[str, List]: ...

class ChatJoinRequest(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    chat: Incomplete
    from_user: Incomplete
    date: Incomplete
    bio: Incomplete
    invite_link: Incomplete
    user_chat_id: Incomplete
    def __init__(self, chat, from_user, user_chat_id, date, bio: Incomplete | None = ..., invite_link: Incomplete | None = ..., **kwargs) -> None: ...

class WebhookInfo(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    url: Incomplete
    has_custom_certificate: Incomplete
    pending_update_count: Incomplete
    ip_address: Incomplete
    last_error_date: Incomplete
    last_error_message: Incomplete
    last_synchronization_error_date: Incomplete
    max_connections: Incomplete
    allowed_updates: Incomplete
    def __init__(self, url, has_custom_certificate, pending_update_count, ip_address: Incomplete | None = ..., last_error_date: Incomplete | None = ..., last_error_message: Incomplete | None = ..., last_synchronization_error_date: Incomplete | None = ..., max_connections: Incomplete | None = ..., allowed_updates: Incomplete | None = ..., **kwargs) -> None: ...

class User(JsonDeserializable, Dictionaryable, JsonSerializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    is_bot: Incomplete
    first_name: Incomplete
    username: Incomplete
    last_name: Incomplete
    language_code: Incomplete
    can_join_groups: Incomplete
    can_read_all_group_messages: Incomplete
    supports_inline_queries: Incomplete
    is_premium: Incomplete
    added_to_attachment_menu: Incomplete
    def __init__(self, id, is_bot, first_name, last_name: Incomplete | None = ..., username: Incomplete | None = ..., language_code: Incomplete | None = ..., can_join_groups: Incomplete | None = ..., can_read_all_group_messages: Incomplete | None = ..., supports_inline_queries: Incomplete | None = ..., is_premium: Incomplete | None = ..., added_to_attachment_menu: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def full_name(self): ...
    def to_json(self): ...
    def to_dict(self): ...

class GroupChat(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title, **kwargs) -> None: ...

class Chat(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    type: Incomplete
    title: Incomplete
    username: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    is_forum: Incomplete
    photo: Incomplete
    bio: Incomplete
    join_to_send_messages: Incomplete
    join_by_request: Incomplete
    has_private_forwards: Incomplete
    has_restricted_voice_and_video_messages: Incomplete
    description: Incomplete
    invite_link: Incomplete
    pinned_message: Incomplete
    permissions: Incomplete
    slow_mode_delay: Incomplete
    message_auto_delete_time: Incomplete
    has_protected_content: Incomplete
    sticker_set_name: Incomplete
    can_set_sticker_set: Incomplete
    linked_chat_id: Incomplete
    location: Incomplete
    active_usernames: Incomplete
    emoji_status_custom_emoji_id: Incomplete
    has_hidden_members: Incomplete
    has_aggressive_anti_spam_enabled: Incomplete
    emoji_status_expiration_date: Incomplete
    def __init__(self, id, type, title: Incomplete | None = ..., username: Incomplete | None = ..., first_name: Incomplete | None = ..., last_name: Incomplete | None = ..., photo: Incomplete | None = ..., bio: Incomplete | None = ..., has_private_forwards: Incomplete | None = ..., description: Incomplete | None = ..., invite_link: Incomplete | None = ..., pinned_message: Incomplete | None = ..., permissions: Incomplete | None = ..., slow_mode_delay: Incomplete | None = ..., message_auto_delete_time: Incomplete | None = ..., has_protected_content: Incomplete | None = ..., sticker_set_name: Incomplete | None = ..., can_set_sticker_set: Incomplete | None = ..., linked_chat_id: Incomplete | None = ..., location: Incomplete | None = ..., join_to_send_messages: Incomplete | None = ..., join_by_request: Incomplete | None = ..., has_restricted_voice_and_video_messages: Incomplete | None = ..., is_forum: Incomplete | None = ..., active_usernames: Incomplete | None = ..., emoji_status_custom_emoji_id: Incomplete | None = ..., has_hidden_members: Incomplete | None = ..., has_aggressive_anti_spam_enabled: Incomplete | None = ..., emoji_status_expiration_date: Incomplete | None = ..., **kwargs) -> None: ...

class MessageID(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    message_id: Incomplete
    def __init__(self, message_id, **kwargs) -> None: ...

class WebAppData(JsonDeserializable, Dictionaryable):
    data: Incomplete
    button_text: Incomplete
    def __init__(self, data, button_text) -> None: ...
    def to_dict(self): ...
    @classmethod
    def de_json(cls, json_string): ...

class Message(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    @classmethod
    def parse_chat(cls, chat): ...
    @classmethod
    def parse_photo(cls, photo_size_array): ...
    @classmethod
    def parse_entities(cls, message_entity_array): ...
    content_type: Incomplete
    id: Incomplete
    message_id: Incomplete
    from_user: Incomplete
    date: Incomplete
    chat: Incomplete
    sender_chat: Incomplete
    forward_from: Incomplete
    forward_from_chat: Incomplete
    forward_from_message_id: Incomplete
    forward_signature: Incomplete
    forward_sender_name: Incomplete
    forward_date: Incomplete
    is_automatic_forward: Incomplete
    reply_to_message: Incomplete
    via_bot: Incomplete
    edit_date: Incomplete
    has_protected_content: Incomplete
    media_group_id: Incomplete
    author_signature: Incomplete
    text: Incomplete
    entities: Incomplete
    caption_entities: Incomplete
    audio: Incomplete
    document: Incomplete
    photo: Incomplete
    sticker: Incomplete
    video: Incomplete
    video_note: Incomplete
    voice: Incomplete
    caption: Incomplete
    contact: Incomplete
    location: Incomplete
    venue: Incomplete
    animation: Incomplete
    dice: Incomplete
    new_chat_member: Incomplete
    new_chat_members: Incomplete
    left_chat_member: Incomplete
    new_chat_title: Incomplete
    new_chat_photo: Incomplete
    delete_chat_photo: Incomplete
    group_chat_created: Incomplete
    supergroup_chat_created: Incomplete
    channel_chat_created: Incomplete
    migrate_to_chat_id: Incomplete
    migrate_from_chat_id: Incomplete
    pinned_message: Incomplete
    invoice: Incomplete
    successful_payment: Incomplete
    connected_website: Incomplete
    reply_markup: Incomplete
    message_thread_id: Incomplete
    is_topic_message: Incomplete
    forum_topic_created: Incomplete
    forum_topic_closed: Incomplete
    forum_topic_reopened: Incomplete
    has_media_spoiler: Incomplete
    forum_topic_edited: Incomplete
    general_forum_topic_hidden: Incomplete
    general_forum_topic_unhidden: Incomplete
    write_access_allowed: Incomplete
    user_shared: Incomplete
    chat_shared: Incomplete
    story: Incomplete
    json: Incomplete
    def __init__(self, message_id, from_user, date, chat, content_type, options, json_string) -> None: ...
    @property
    def html_text(self): ...
    @property
    def html_caption(self): ...

class MessageEntity(Dictionaryable, JsonSerializable, JsonDeserializable):
    @staticmethod
    def to_list_of_dicts(entity_list) -> Union[List[Dict], None]: ...
    @classmethod
    def de_json(cls, json_string): ...
    type: Incomplete
    offset: Incomplete
    length: Incomplete
    url: Incomplete
    user: Incomplete
    language: Incomplete
    custom_emoji_id: Incomplete
    def __init__(self, type, offset, length, url: Incomplete | None = ..., user: Incomplete | None = ..., language: Incomplete | None = ..., custom_emoji_id: Incomplete | None = ..., **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class Dice(JsonSerializable, Dictionaryable, JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    value: Incomplete
    emoji: Incomplete
    def __init__(self, value, emoji, **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class PhotoSize(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    width: Incomplete
    height: Incomplete
    file_size: Incomplete
    def __init__(self, file_id, file_unique_id, width, height, file_size: Incomplete | None = ..., **kwargs) -> None: ...

class Audio(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    duration: Incomplete
    performer: Incomplete
    title: Incomplete
    file_name: Incomplete
    mime_type: Incomplete
    file_size: Incomplete
    thumbnail: Incomplete
    def __init__(self, file_id, file_unique_id, duration, performer: Incomplete | None = ..., title: Incomplete | None = ..., file_name: Incomplete | None = ..., mime_type: Incomplete | None = ..., file_size: Incomplete | None = ..., thumbnail: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def thumb(self): ...

class Voice(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    duration: Incomplete
    mime_type: Incomplete
    file_size: Incomplete
    def __init__(self, file_id, file_unique_id, duration, mime_type: Incomplete | None = ..., file_size: Incomplete | None = ..., **kwargs) -> None: ...

class Document(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    thumbnail: Incomplete
    file_name: Incomplete
    mime_type: Incomplete
    file_size: Incomplete
    def __init__(self, file_id, file_unique_id, thumbnail: Incomplete | None = ..., file_name: Incomplete | None = ..., mime_type: Incomplete | None = ..., file_size: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def thumb(self): ...

class Video(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    width: Incomplete
    height: Incomplete
    duration: Incomplete
    thumbnail: Incomplete
    file_name: Incomplete
    mime_type: Incomplete
    file_size: Incomplete
    def __init__(self, file_id, file_unique_id, width, height, duration, thumbnail: Incomplete | None = ..., file_name: Incomplete | None = ..., mime_type: Incomplete | None = ..., file_size: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def thumb(self): ...

class VideoNote(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    length: Incomplete
    duration: Incomplete
    thumbnail: Incomplete
    file_size: Incomplete
    def __init__(self, file_id, file_unique_id, length, duration, thumbnail: Incomplete | None = ..., file_size: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def thumb(self): ...

class Contact(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    phone_number: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    user_id: Incomplete
    vcard: Incomplete
    def __init__(self, phone_number, first_name, last_name: Incomplete | None = ..., user_id: Incomplete | None = ..., vcard: Incomplete | None = ..., **kwargs) -> None: ...

class Location(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    longitude: Incomplete
    latitude: Incomplete
    horizontal_accuracy: Incomplete
    live_period: Incomplete
    heading: Incomplete
    proximity_alert_radius: Incomplete
    def __init__(self, longitude, latitude, horizontal_accuracy: Incomplete | None = ..., live_period: Incomplete | None = ..., heading: Incomplete | None = ..., proximity_alert_radius: Incomplete | None = ..., **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class Venue(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    location: Incomplete
    title: Incomplete
    address: Incomplete
    foursquare_id: Incomplete
    foursquare_type: Incomplete
    google_place_id: Incomplete
    google_place_type: Incomplete
    def __init__(self, location, title, address, foursquare_id: Incomplete | None = ..., foursquare_type: Incomplete | None = ..., google_place_id: Incomplete | None = ..., google_place_type: Incomplete | None = ..., **kwargs) -> None: ...

class UserProfilePhotos(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    total_count: Incomplete
    photos: Incomplete
    def __init__(self, total_count, photos: Incomplete | None = ..., **kwargs) -> None: ...

class File(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    file_size: Incomplete
    file_path: Incomplete
    def __init__(self, file_id, file_unique_id, file_size: Incomplete | None = ..., file_path: Incomplete | None = ..., **kwargs) -> None: ...

class ForceReply(JsonSerializable):
    selective: Incomplete
    input_field_placeholder: Incomplete
    def __init__(self, selective: Optional[bool] = ..., input_field_placeholder: Optional[str] = ...) -> None: ...
    def to_json(self): ...

class ReplyKeyboardRemove(JsonSerializable):
    selective: Incomplete
    def __init__(self, selective: Incomplete | None = ...) -> None: ...
    def to_json(self): ...

class WebAppInfo(JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    url: Incomplete
    def __init__(self, url, **kwargs) -> None: ...
    def to_dict(self): ...

class ReplyKeyboardMarkup(JsonSerializable):
    max_row_keys: int
    resize_keyboard: Incomplete
    one_time_keyboard: Incomplete
    selective: Incomplete
    row_width: Incomplete
    input_field_placeholder: Incomplete
    keyboard: Incomplete
    is_persistent: Incomplete
    def __init__(self, resize_keyboard: Optional[bool] = ..., one_time_keyboard: Optional[bool] = ..., selective: Optional[bool] = ..., row_width: int = ..., input_field_placeholder: Optional[str] = ..., is_persistent: Optional[bool] = ...) -> None: ...
    def add(self, *args, row_width: Incomplete | None = ...): ...
    def row(self, *args): ...
    def to_json(self): ...

class KeyboardButtonPollType(Dictionaryable):
    type: Incomplete
    def __init__(self, type: str = ...) -> None: ...
    def to_dict(self): ...

class KeyboardButtonRequestUser(Dictionaryable):
    request_id: Incomplete
    user_is_bot: Incomplete
    user_is_premium: Incomplete
    def __init__(self, request_id: int, user_is_bot: Optional[bool] = ..., user_is_premium: Optional[bool] = ...) -> None: ...
    def to_dict(self) -> dict: ...

class KeyboardButtonRequestChat(Dictionaryable):
    request_id: Incomplete
    chat_is_channel: Incomplete
    chat_is_forum: Incomplete
    chat_has_username: Incomplete
    chat_is_created: Incomplete
    user_administrator_rights: Incomplete
    bot_administrator_rights: Incomplete
    bot_is_member: Incomplete
    def __init__(self, request_id: int, chat_is_channel: bool, chat_is_forum: Optional[bool] = ..., chat_has_username: Optional[bool] = ..., chat_is_created: Optional[bool] = ..., user_administrator_rights: Optional[ChatAdministratorRights] = ..., bot_administrator_rights: Optional[ChatAdministratorRights] = ..., bot_is_member: Optional[bool] = ...) -> None: ...
    def to_dict(self) -> dict: ...

class KeyboardButton(Dictionaryable, JsonSerializable):
    text: Incomplete
    request_contact: Incomplete
    request_location: Incomplete
    request_poll: Incomplete
    web_app: Incomplete
    request_user: Incomplete
    request_chat: Incomplete
    def __init__(self, text: str, request_contact: Optional[bool] = ..., request_location: Optional[bool] = ..., request_poll: Optional[KeyboardButtonPollType] = ..., web_app: Optional[WebAppInfo] = ..., request_user: Optional[KeyboardButtonRequestUser] = ..., request_chat: Optional[KeyboardButtonRequestChat] = ...) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class InlineKeyboardMarkup(Dictionaryable, JsonSerializable, JsonDeserializable):
    max_row_keys: int
    @classmethod
    def de_json(cls, json_string): ...
    row_width: Incomplete
    keyboard: Incomplete
    def __init__(self, keyboard: Incomplete | None = ..., row_width: int = ...) -> None: ...
    def add(self, *args, row_width: Incomplete | None = ...): ...
    def row(self, *args): ...
    def to_json(self): ...
    def to_dict(self): ...

class InlineKeyboardButton(Dictionaryable, JsonSerializable, JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    text: Incomplete
    url: Incomplete
    callback_data: Incomplete
    web_app: Incomplete
    switch_inline_query: Incomplete
    switch_inline_query_current_chat: Incomplete
    switch_inline_query_chosen_chat: Incomplete
    callback_game: Incomplete
    pay: Incomplete
    login_url: Incomplete
    def __init__(self, text, url: Incomplete | None = ..., callback_data: Incomplete | None = ..., web_app: Incomplete | None = ..., switch_inline_query: Incomplete | None = ..., switch_inline_query_current_chat: Incomplete | None = ..., switch_inline_query_chosen_chat: Incomplete | None = ..., callback_game: Incomplete | None = ..., pay: Incomplete | None = ..., login_url: Incomplete | None = ..., **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class LoginUrl(Dictionaryable, JsonSerializable, JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    url: Incomplete
    forward_text: Incomplete
    bot_username: Incomplete
    request_write_access: Incomplete
    def __init__(self, url, forward_text: Incomplete | None = ..., bot_username: Incomplete | None = ..., request_write_access: Incomplete | None = ..., **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class CallbackQuery(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    from_user: Incomplete
    message: Incomplete
    inline_message_id: Incomplete
    chat_instance: Incomplete
    data: Incomplete
    game_short_name: Incomplete
    json: Incomplete
    def __init__(self, id, from_user, data, chat_instance, json_string, message: Incomplete | None = ..., inline_message_id: Incomplete | None = ..., game_short_name: Incomplete | None = ..., **kwargs) -> None: ...

class ChatPhoto(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    small_file_id: Incomplete
    small_file_unique_id: Incomplete
    big_file_id: Incomplete
    big_file_unique_id: Incomplete
    def __init__(self, small_file_id, small_file_unique_id, big_file_id, big_file_unique_id, **kwargs) -> None: ...

class ChatMember(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    user: Incomplete
    status: Incomplete
    custom_title: Incomplete
    is_anonymous: Incomplete
    can_be_edited: Incomplete
    can_post_messages: Incomplete
    can_edit_messages: Incomplete
    can_delete_messages: Incomplete
    can_restrict_members: Incomplete
    can_promote_members: Incomplete
    can_change_info: Incomplete
    can_invite_users: Incomplete
    can_pin_messages: Incomplete
    is_member: Incomplete
    can_send_messages: Incomplete
    can_send_polls: Incomplete
    can_send_other_messages: Incomplete
    can_add_web_page_previews: Incomplete
    can_manage_chat: Incomplete
    can_manage_video_chats: Incomplete
    can_manage_voice_chats: Incomplete
    until_date: Incomplete
    can_manage_topics: Incomplete
    can_send_audios: Incomplete
    can_send_documents: Incomplete
    can_send_photos: Incomplete
    can_send_videos: Incomplete
    can_send_video_notes: Incomplete
    can_send_voice_notes: Incomplete
    can_post_stories: Incomplete
    can_edit_stories: Incomplete
    can_delete_stories: Incomplete
    def __init__(self, user, status, custom_title: Incomplete | None = ..., is_anonymous: Incomplete | None = ..., can_be_edited: Incomplete | None = ..., can_post_messages: Incomplete | None = ..., can_edit_messages: Incomplete | None = ..., can_delete_messages: Incomplete | None = ..., can_restrict_members: Incomplete | None = ..., can_promote_members: Incomplete | None = ..., can_change_info: Incomplete | None = ..., can_invite_users: Incomplete | None = ..., can_pin_messages: Incomplete | None = ..., is_member: Incomplete | None = ..., can_send_messages: Incomplete | None = ..., can_send_audios: Incomplete | None = ..., can_send_documents: Incomplete | None = ..., can_send_photos: Incomplete | None = ..., can_send_videos: Incomplete | None = ..., can_send_video_notes: Incomplete | None = ..., can_send_voice_notes: Incomplete | None = ..., can_send_polls: Incomplete | None = ..., can_send_other_messages: Incomplete | None = ..., can_add_web_page_previews: Incomplete | None = ..., can_manage_chat: Incomplete | None = ..., can_manage_video_chats: Incomplete | None = ..., until_date: Incomplete | None = ..., can_manage_topics: Incomplete | None = ..., can_post_stories: Incomplete | None = ..., can_edit_stories: Incomplete | None = ..., can_delete_stories: Incomplete | None = ..., **kwargs) -> None: ...

class ChatMemberOwner(ChatMember): ...
class ChatMemberAdministrator(ChatMember): ...
class ChatMemberMember(ChatMember): ...
class ChatMemberRestricted(ChatMember): ...
class ChatMemberLeft(ChatMember): ...
class ChatMemberBanned(ChatMember): ...

class ChatPermissions(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    can_send_messages: Incomplete
    can_send_polls: Incomplete
    can_send_other_messages: Incomplete
    can_add_web_page_previews: Incomplete
    can_change_info: Incomplete
    can_invite_users: Incomplete
    can_pin_messages: Incomplete
    can_manage_topics: Incomplete
    can_send_audios: Incomplete
    can_send_documents: Incomplete
    can_send_photos: Incomplete
    can_send_videos: Incomplete
    can_send_video_notes: Incomplete
    can_send_voice_notes: Incomplete
    def __init__(self, can_send_messages: Incomplete | None = ..., can_send_media_messages: Incomplete | None = ..., can_send_audios: Incomplete | None = ..., can_send_documents: Incomplete | None = ..., can_send_photos: Incomplete | None = ..., can_send_videos: Incomplete | None = ..., can_send_video_notes: Incomplete | None = ..., can_send_voice_notes: Incomplete | None = ..., can_send_polls: Incomplete | None = ..., can_send_other_messages: Incomplete | None = ..., can_add_web_page_previews: Incomplete | None = ..., can_change_info: Incomplete | None = ..., can_invite_users: Incomplete | None = ..., can_pin_messages: Incomplete | None = ..., can_manage_topics: Incomplete | None = ..., **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class BotCommand(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    command: Incomplete
    description: Incomplete
    def __init__(self, command, description) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class BotCommandScope(ABC, JsonSerializable):
    type: Incomplete
    chat_id: Incomplete
    user_id: Incomplete
    def __init__(self, type: str = ..., chat_id: Incomplete | None = ..., user_id: Incomplete | None = ...) -> None: ...
    def to_json(self): ...

class BotCommandScopeDefault(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeAllPrivateChats(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeAllGroupChats(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeAllChatAdministrators(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeChat(BotCommandScope):
    def __init__(self, chat_id: Incomplete | None = ...) -> None: ...

class BotCommandScopeChatAdministrators(BotCommandScope):
    def __init__(self, chat_id: Incomplete | None = ...) -> None: ...

class BotCommandScopeChatMember(BotCommandScope):
    def __init__(self, chat_id: Incomplete | None = ..., user_id: Incomplete | None = ...) -> None: ...

class InlineQuery(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    from_user: Incomplete
    query: Incomplete
    offset: Incomplete
    chat_type: Incomplete
    location: Incomplete
    def __init__(self, id, from_user, query, offset, chat_type: Incomplete | None = ..., location: Incomplete | None = ..., **kwargs) -> None: ...

class InputTextMessageContent(Dictionaryable):
    message_text: Incomplete
    parse_mode: Incomplete
    entities: Incomplete
    disable_web_page_preview: Incomplete
    def __init__(self, message_text, parse_mode: Incomplete | None = ..., entities: Incomplete | None = ..., disable_web_page_preview: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InputLocationMessageContent(Dictionaryable):
    latitude: Incomplete
    longitude: Incomplete
    horizontal_accuracy: Incomplete
    live_period: Incomplete
    heading: Incomplete
    proximity_alert_radius: Incomplete
    def __init__(self, latitude, longitude, horizontal_accuracy: Incomplete | None = ..., live_period: Incomplete | None = ..., heading: Incomplete | None = ..., proximity_alert_radius: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InputVenueMessageContent(Dictionaryable):
    latitude: Incomplete
    longitude: Incomplete
    title: Incomplete
    address: Incomplete
    foursquare_id: Incomplete
    foursquare_type: Incomplete
    google_place_id: Incomplete
    google_place_type: Incomplete
    def __init__(self, latitude, longitude, title, address, foursquare_id: Incomplete | None = ..., foursquare_type: Incomplete | None = ..., google_place_id: Incomplete | None = ..., google_place_type: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InputContactMessageContent(Dictionaryable):
    phone_number: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    vcard: Incomplete
    def __init__(self, phone_number, first_name, last_name: Incomplete | None = ..., vcard: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InputInvoiceMessageContent(Dictionaryable):
    title: Incomplete
    description: Incomplete
    payload: Incomplete
    provider_token: Incomplete
    currency: Incomplete
    prices: Incomplete
    max_tip_amount: Incomplete
    suggested_tip_amounts: Incomplete
    provider_data: Incomplete
    photo_url: Incomplete
    photo_size: Incomplete
    photo_width: Incomplete
    photo_height: Incomplete
    need_name: Incomplete
    need_phone_number: Incomplete
    need_email: Incomplete
    need_shipping_address: Incomplete
    send_phone_number_to_provider: Incomplete
    send_email_to_provider: Incomplete
    is_flexible: Incomplete
    def __init__(self, title, description, payload, provider_token, currency, prices, max_tip_amount: Incomplete | None = ..., suggested_tip_amounts: Incomplete | None = ..., provider_data: Incomplete | None = ..., photo_url: Incomplete | None = ..., photo_size: Incomplete | None = ..., photo_width: Incomplete | None = ..., photo_height: Incomplete | None = ..., need_name: Incomplete | None = ..., need_phone_number: Incomplete | None = ..., need_email: Incomplete | None = ..., need_shipping_address: Incomplete | None = ..., send_phone_number_to_provider: Incomplete | None = ..., send_email_to_provider: Incomplete | None = ..., is_flexible: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class ChosenInlineResult(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    result_id: Incomplete
    from_user: Incomplete
    location: Incomplete
    inline_message_id: Incomplete
    query: Incomplete
    def __init__(self, result_id, from_user, query, location: Incomplete | None = ..., inline_message_id: Incomplete | None = ..., **kwargs) -> None: ...

class InlineQueryResultBase(ABC, Dictionaryable, JsonSerializable):
    type: Incomplete
    id: Incomplete
    title: Incomplete
    caption: Incomplete
    input_message_content: Incomplete
    reply_markup: Incomplete
    caption_entities: Incomplete
    parse_mode: Incomplete
    def __init__(self, type, id, title: Incomplete | None = ..., caption: Incomplete | None = ..., input_message_content: Incomplete | None = ..., reply_markup: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ...) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class SentWebAppMessage(JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    inline_message_id: Incomplete
    def __init__(self, inline_message_id: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InlineQueryResultArticle(InlineQueryResultBase):
    url: Incomplete
    hide_url: Incomplete
    description: Incomplete
    thumbnail_url: Incomplete
    thumbnail_width: Incomplete
    thumbnail_height: Incomplete
    def __init__(self, id, title, input_message_content, reply_markup: Incomplete | None = ..., url: Incomplete | None = ..., hide_url: Incomplete | None = ..., description: Incomplete | None = ..., thumbnail_url: Incomplete | None = ..., thumbnail_width: Incomplete | None = ..., thumbnail_height: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    @property
    def thumb_width(self): ...
    @property
    def thumb_height(self): ...
    def to_dict(self): ...

class InlineQueryResultPhoto(InlineQueryResultBase):
    photo_url: Incomplete
    thumbnail_url: Incomplete
    photo_width: Incomplete
    photo_height: Incomplete
    description: Incomplete
    def __init__(self, id, photo_url, thumbnail_url, photo_width: Incomplete | None = ..., photo_height: Incomplete | None = ..., title: Incomplete | None = ..., description: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    def to_dict(self): ...

class InlineQueryResultGif(InlineQueryResultBase):
    gif_url: Incomplete
    gif_width: Incomplete
    gif_height: Incomplete
    thumbnail_url: Incomplete
    gif_duration: Incomplete
    thumbnail_mime_type: Incomplete
    def __init__(self, id, gif_url, thumbnail_url, gif_width: Incomplete | None = ..., gif_height: Incomplete | None = ..., title: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ..., gif_duration: Incomplete | None = ..., parse_mode: Incomplete | None = ..., thumbnail_mime_type: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    @property
    def thumb_mime_type(self): ...
    def to_dict(self): ...

class InlineQueryResultMpeg4Gif(InlineQueryResultBase):
    mpeg4_url: Incomplete
    mpeg4_width: Incomplete
    mpeg4_height: Incomplete
    thumbnail_url: Incomplete
    mpeg4_duration: Incomplete
    thumbnail_mime_type: Incomplete
    def __init__(self, id, mpeg4_url, thumbnail_url, mpeg4_width: Incomplete | None = ..., mpeg4_height: Incomplete | None = ..., title: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ..., mpeg4_duration: Incomplete | None = ..., thumbnail_mime_type: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    @property
    def thumb_mime_type(self): ...
    def to_dict(self): ...

class InlineQueryResultVideo(InlineQueryResultBase):
    video_url: Incomplete
    mime_type: Incomplete
    thumbnail_url: Incomplete
    video_width: Incomplete
    video_height: Incomplete
    video_duration: Incomplete
    description: Incomplete
    def __init__(self, id, video_url, mime_type, thumbnail_url, title, caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., video_width: Incomplete | None = ..., video_height: Incomplete | None = ..., video_duration: Incomplete | None = ..., description: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    def to_dict(self): ...

class InlineQueryResultAudio(InlineQueryResultBase):
    audio_url: Incomplete
    performer: Incomplete
    audio_duration: Incomplete
    def __init__(self, id, audio_url, title, caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., performer: Incomplete | None = ..., audio_duration: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InlineQueryResultVoice(InlineQueryResultBase):
    voice_url: Incomplete
    voice_duration: Incomplete
    def __init__(self, id, voice_url, title, caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., voice_duration: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InlineQueryResultDocument(InlineQueryResultBase):
    document_url: Incomplete
    mime_type: Incomplete
    description: Incomplete
    thumbnail_url: Incomplete
    thumbnail_width: Incomplete
    thumbnail_height: Incomplete
    def __init__(self, id, title, document_url, mime_type, caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., description: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ..., thumbnail_url: Incomplete | None = ..., thumbnail_width: Incomplete | None = ..., thumbnail_height: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    @property
    def thumb_width(self): ...
    @property
    def thumb_height(self): ...
    def to_dict(self): ...

class InlineQueryResultLocation(InlineQueryResultBase):
    latitude: Incomplete
    longitude: Incomplete
    horizontal_accuracy: Incomplete
    live_period: Incomplete
    heading: Incomplete
    proximity_alert_radius: Incomplete
    thumbnail_url: Incomplete
    thumbnail_width: Incomplete
    thumbnail_height: Incomplete
    def __init__(self, id, title, latitude, longitude, horizontal_accuracy, live_period: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ..., thumbnail_url: Incomplete | None = ..., thumbnail_width: Incomplete | None = ..., thumbnail_height: Incomplete | None = ..., heading: Incomplete | None = ..., proximity_alert_radius: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    @property
    def thumb_width(self): ...
    @property
    def thumb_height(self): ...
    def to_dict(self): ...

class InlineQueryResultVenue(InlineQueryResultBase):
    latitude: Incomplete
    longitude: Incomplete
    address: Incomplete
    foursquare_id: Incomplete
    foursquare_type: Incomplete
    google_place_id: Incomplete
    google_place_type: Incomplete
    thumbnail_url: Incomplete
    thumbnail_width: Incomplete
    thumbnail_height: Incomplete
    def __init__(self, id, title, latitude, longitude, address, foursquare_id: Incomplete | None = ..., foursquare_type: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ..., thumbnail_url: Incomplete | None = ..., thumbnail_width: Incomplete | None = ..., thumbnail_height: Incomplete | None = ..., google_place_id: Incomplete | None = ..., google_place_type: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    @property
    def thumb_width(self): ...
    @property
    def thumb_height(self): ...
    def to_dict(self): ...

class InlineQueryResultContact(InlineQueryResultBase):
    phone_number: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    vcard: Incomplete
    thumbnail_url: Incomplete
    thumbnail_width: Incomplete
    thumbnail_height: Incomplete
    def __init__(self, id, phone_number, first_name, last_name: Incomplete | None = ..., vcard: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ..., thumbnail_url: Incomplete | None = ..., thumbnail_width: Incomplete | None = ..., thumbnail_height: Incomplete | None = ...) -> None: ...
    @property
    def thumb_url(self): ...
    @property
    def thumb_width(self): ...
    @property
    def thumb_height(self): ...
    def to_dict(self): ...

class InlineQueryResultGame(InlineQueryResultBase):
    game_short_name: Incomplete
    def __init__(self, id, game_short_name, reply_markup: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InlineQueryResultCachedBase(ABC, JsonSerializable):
    type: Incomplete
    id: Incomplete
    title: Incomplete
    description: Incomplete
    caption: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    caption_entities: Incomplete
    payload_dic: Incomplete
    def __init__(self) -> None: ...
    def to_json(self): ...

class InlineQueryResultCachedPhoto(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    photo_file_id: Incomplete
    title: Incomplete
    description: Incomplete
    caption: Incomplete
    caption_entities: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    def __init__(self, id, photo_file_id, title: Incomplete | None = ..., description: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class InlineQueryResultCachedGif(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    gif_file_id: Incomplete
    title: Incomplete
    description: Incomplete
    caption: Incomplete
    caption_entities: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    def __init__(self, id, gif_file_id, title: Incomplete | None = ..., description: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class InlineQueryResultCachedMpeg4Gif(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    mpeg4_file_id: Incomplete
    title: Incomplete
    description: Incomplete
    caption: Incomplete
    caption_entities: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    def __init__(self, id, mpeg4_file_id, title: Incomplete | None = ..., description: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class InlineQueryResultCachedSticker(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    sticker_file_id: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    def __init__(self, id, sticker_file_id, reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class InlineQueryResultCachedDocument(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    document_file_id: Incomplete
    title: Incomplete
    description: Incomplete
    caption: Incomplete
    caption_entities: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    def __init__(self, id, document_file_id, title, description: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class InlineQueryResultCachedVideo(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    video_file_id: Incomplete
    title: Incomplete
    description: Incomplete
    caption: Incomplete
    caption_entities: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    def __init__(self, id, video_file_id, title, description: Incomplete | None = ..., caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class InlineQueryResultCachedVoice(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    voice_file_id: Incomplete
    title: Incomplete
    caption: Incomplete
    caption_entities: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    def __init__(self, id, voice_file_id, title, caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class InlineQueryResultCachedAudio(InlineQueryResultCachedBase):
    type: str
    id: Incomplete
    audio_file_id: Incomplete
    caption: Incomplete
    caption_entities: Incomplete
    reply_markup: Incomplete
    input_message_content: Incomplete
    parse_mode: Incomplete
    def __init__(self, id, audio_file_id, caption: Incomplete | None = ..., caption_entities: Incomplete | None = ..., parse_mode: Incomplete | None = ..., reply_markup: Incomplete | None = ..., input_message_content: Incomplete | None = ...) -> None: ...

class Game(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    @classmethod
    def parse_photo(cls, photo_size_array): ...
    @classmethod
    def parse_entities(cls, message_entity_array): ...
    title: Incomplete
    description: Incomplete
    photo: Incomplete
    text: Incomplete
    text_entities: Incomplete
    animation: Incomplete
    def __init__(self, title, description, photo, text: Incomplete | None = ..., text_entities: Incomplete | None = ..., animation: Incomplete | None = ..., **kwargs) -> None: ...

class Animation(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    width: Incomplete
    height: Incomplete
    duration: Incomplete
    thumbnail: Incomplete
    file_name: Incomplete
    mime_type: Incomplete
    file_size: Incomplete
    def __init__(self, file_id, file_unique_id, width: Incomplete | None = ..., height: Incomplete | None = ..., duration: Incomplete | None = ..., thumbnail: Incomplete | None = ..., file_name: Incomplete | None = ..., mime_type: Incomplete | None = ..., file_size: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def thumb(self): ...

class GameHighScore(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    position: Incomplete
    user: Incomplete
    score: Incomplete
    def __init__(self, position, user, score, **kwargs) -> None: ...

class LabeledPrice(JsonSerializable, Dictionaryable):
    label: Incomplete
    amount: Incomplete
    def __init__(self, label, amount) -> None: ...
    def to_dict(self): ...
    def to_json(self): ...

class Invoice(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    title: Incomplete
    description: Incomplete
    start_parameter: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    def __init__(self, title, description, start_parameter, currency, total_amount, **kwargs) -> None: ...

class ShippingAddress(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    country_code: Incomplete
    state: Incomplete
    city: Incomplete
    street_line1: Incomplete
    street_line2: Incomplete
    post_code: Incomplete
    def __init__(self, country_code, state, city, street_line1, street_line2, post_code, **kwargs) -> None: ...

class OrderInfo(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    name: Incomplete
    phone_number: Incomplete
    email: Incomplete
    shipping_address: Incomplete
    def __init__(self, name: Incomplete | None = ..., phone_number: Incomplete | None = ..., email: Incomplete | None = ..., shipping_address: Incomplete | None = ..., **kwargs) -> None: ...

class ShippingOption(JsonSerializable):
    id: Incomplete
    title: Incomplete
    prices: Incomplete
    def __init__(self, id, title) -> None: ...
    def add_price(self, *args): ...
    def to_json(self): ...

class SuccessfulPayment(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    currency: Incomplete
    total_amount: Incomplete
    invoice_payload: Incomplete
    shipping_option_id: Incomplete
    order_info: Incomplete
    telegram_payment_charge_id: Incomplete
    provider_payment_charge_id: Incomplete
    def __init__(self, currency, total_amount, invoice_payload, shipping_option_id: Incomplete | None = ..., order_info: Incomplete | None = ..., telegram_payment_charge_id: Incomplete | None = ..., provider_payment_charge_id: Incomplete | None = ..., **kwargs) -> None: ...

class ShippingQuery(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    from_user: Incomplete
    invoice_payload: Incomplete
    shipping_address: Incomplete
    def __init__(self, id, from_user, invoice_payload, shipping_address, **kwargs) -> None: ...

class PreCheckoutQuery(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    from_user: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    invoice_payload: Incomplete
    shipping_option_id: Incomplete
    order_info: Incomplete
    def __init__(self, id, from_user, currency, total_amount, invoice_payload, shipping_option_id: Incomplete | None = ..., order_info: Incomplete | None = ..., **kwargs) -> None: ...

class StickerSet(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    name: Incomplete
    title: Incomplete
    sticker_type: Incomplete
    is_animated: Incomplete
    is_video: Incomplete
    stickers: Incomplete
    thumbnail: Incomplete
    def __init__(self, name, title, sticker_type, is_animated, is_video, stickers, thumbnail: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def thumb(self): ...
    @property
    def contains_masks(self): ...

class Sticker(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    file_id: Incomplete
    file_unique_id: Incomplete
    type: Incomplete
    width: Incomplete
    height: Incomplete
    is_animated: Incomplete
    is_video: Incomplete
    thumbnail: Incomplete
    emoji: Incomplete
    set_name: Incomplete
    mask_position: Incomplete
    file_size: Incomplete
    premium_animation: Incomplete
    custom_emoji_id: Incomplete
    needs_repainting: Incomplete
    def __init__(self, file_id, file_unique_id, type, width, height, is_animated, is_video, thumbnail: Incomplete | None = ..., emoji: Incomplete | None = ..., set_name: Incomplete | None = ..., mask_position: Incomplete | None = ..., file_size: Incomplete | None = ..., premium_animation: Incomplete | None = ..., custom_emoji_id: Incomplete | None = ..., needs_repainting: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def thumb(self): ...

class MaskPosition(Dictionaryable, JsonDeserializable, JsonSerializable):
    @classmethod
    def de_json(cls, json_string): ...
    point: Incomplete
    x_shift: Incomplete
    y_shift: Incomplete
    scale: Incomplete
    def __init__(self, point, x_shift, y_shift, scale, **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class InputMedia(Dictionaryable, JsonSerializable):
    type: Incomplete
    media: Incomplete
    caption: Incomplete
    parse_mode: Incomplete
    caption_entities: Incomplete
    def __init__(self, type, media, caption: Incomplete | None = ..., parse_mode: Incomplete | None = ..., caption_entities: Incomplete | None = ...) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...
    def convert_input_media(self): ...

class InputMediaPhoto(InputMedia):
    has_spoiler: Incomplete
    def __init__(self, media, caption: Incomplete | None = ..., parse_mode: Incomplete | None = ..., caption_entities: Incomplete | None = ..., has_spoiler: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class InputMediaVideo(InputMedia):
    thumbnail: Incomplete
    width: Incomplete
    height: Incomplete
    duration: Incomplete
    supports_streaming: Incomplete
    has_spoiler: Incomplete
    def __init__(self, media, thumbnail: Incomplete | None = ..., caption: Incomplete | None = ..., parse_mode: Incomplete | None = ..., caption_entities: Incomplete | None = ..., width: Incomplete | None = ..., height: Incomplete | None = ..., duration: Incomplete | None = ..., supports_streaming: Incomplete | None = ..., has_spoiler: Incomplete | None = ...) -> None: ...
    @property
    def thumb(self): ...
    def to_dict(self): ...

class InputMediaAnimation(InputMedia):
    thumbnail: Incomplete
    width: Incomplete
    height: Incomplete
    duration: Incomplete
    has_spoiler: Incomplete
    def __init__(self, media, thumbnail: Incomplete | None = ..., caption: Incomplete | None = ..., parse_mode: Incomplete | None = ..., caption_entities: Incomplete | None = ..., width: Incomplete | None = ..., height: Incomplete | None = ..., duration: Incomplete | None = ..., has_spoiler: Incomplete | None = ...) -> None: ...
    @property
    def thumb(self): ...
    def to_dict(self): ...

class InputMediaAudio(InputMedia):
    thumbnail: Incomplete
    duration: Incomplete
    performer: Incomplete
    title: Incomplete
    def __init__(self, media, thumbnail: Incomplete | None = ..., caption: Incomplete | None = ..., parse_mode: Incomplete | None = ..., caption_entities: Incomplete | None = ..., duration: Incomplete | None = ..., performer: Incomplete | None = ..., title: Incomplete | None = ...) -> None: ...
    @property
    def thumb(self): ...
    def to_dict(self): ...

class InputMediaDocument(InputMedia):
    thumbnail: Incomplete
    disable_content_type_detection: Incomplete
    def __init__(self, media, thumbnail: Incomplete | None = ..., caption: Incomplete | None = ..., parse_mode: Incomplete | None = ..., caption_entities: Incomplete | None = ..., disable_content_type_detection: Incomplete | None = ...) -> None: ...
    @property
    def thumb(self): ...
    def to_dict(self): ...

class PollOption(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    text: Incomplete
    voter_count: Incomplete
    def __init__(self, text, voter_count: int = ..., **kwargs) -> None: ...

class Poll(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    id: Incomplete
    question: Incomplete
    options: Incomplete
    total_voter_count: Incomplete
    is_closed: Incomplete
    is_anonymous: Incomplete
    type: Incomplete
    allows_multiple_answers: Incomplete
    correct_option_id: Incomplete
    explanation: Incomplete
    explanation_entities: Incomplete
    open_period: Incomplete
    close_date: Incomplete
    def __init__(self, question, options, poll_id: Incomplete | None = ..., total_voter_count: Incomplete | None = ..., is_closed: Incomplete | None = ..., is_anonymous: Incomplete | None = ..., type: Incomplete | None = ..., allows_multiple_answers: Incomplete | None = ..., correct_option_id: Incomplete | None = ..., explanation: Incomplete | None = ..., explanation_entities: Incomplete | None = ..., open_period: Incomplete | None = ..., close_date: Incomplete | None = ..., poll_type: Incomplete | None = ..., **kwargs) -> None: ...
    def add(self, option) -> None: ...

class PollAnswer(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    poll_id: Incomplete
    user: Incomplete
    option_ids: Incomplete
    voter_chat: Incomplete
    def __init__(self, poll_id, option_ids, user: Incomplete | None = ..., voter_chat: Incomplete | None = ..., **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class ChatLocation(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    location: Incomplete
    address: Incomplete
    def __init__(self, location, address, **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class ChatInviteLink(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    invite_link: Incomplete
    creator: Incomplete
    creates_join_request: Incomplete
    is_primary: Incomplete
    is_revoked: Incomplete
    name: Incomplete
    expire_date: Incomplete
    member_limit: Incomplete
    pending_join_request_count: Incomplete
    def __init__(self, invite_link, creator, creates_join_request, is_primary, is_revoked, name: Incomplete | None = ..., expire_date: Incomplete | None = ..., member_limit: Incomplete | None = ..., pending_join_request_count: Incomplete | None = ..., **kwargs) -> None: ...
    def to_json(self): ...
    def to_dict(self): ...

class ProximityAlertTriggered(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    traveler: Incomplete
    watcher: Incomplete
    distance: Incomplete
    def __init__(self, traveler, watcher, distance, **kwargs) -> None: ...

class VideoChatStarted(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    def __init__(self) -> None: ...

class VoiceChatStarted(VideoChatStarted):
    def __init__(self) -> None: ...

class VideoChatScheduled(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    start_date: Incomplete
    def __init__(self, start_date, **kwargs) -> None: ...

class VoiceChatScheduled(VideoChatScheduled):
    def __init__(self, *args, **kwargs) -> None: ...

class VideoChatEnded(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    duration: Incomplete
    def __init__(self, duration, **kwargs) -> None: ...

class VoiceChatEnded(VideoChatEnded):
    def __init__(self, *args, **kwargs) -> None: ...

class VideoChatParticipantsInvited(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    users: Incomplete
    def __init__(self, users: Incomplete | None = ..., **kwargs) -> None: ...

class VoiceChatParticipantsInvited(VideoChatParticipantsInvited):
    def __init__(self, *args, **kwargs) -> None: ...

class MessageAutoDeleteTimerChanged(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    message_auto_delete_time: Incomplete
    def __init__(self, message_auto_delete_time, **kwargs) -> None: ...

class MenuButton(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    def to_json(self) -> None: ...
    def to_dict(self) -> None: ...

class MenuButtonCommands(MenuButton):
    type: Incomplete
    def __init__(self, type) -> None: ...
    def to_dict(self): ...
    def to_json(self): ...

class MenuButtonWebApp(MenuButton):
    type: Incomplete
    text: Incomplete
    web_app: Incomplete
    def __init__(self, type, text, web_app) -> None: ...
    def to_dict(self): ...
    def to_json(self): ...

class MenuButtonDefault(MenuButton):
    type: Incomplete
    def __init__(self, type) -> None: ...
    def to_dict(self): ...
    def to_json(self): ...

class ChatAdministratorRights(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string): ...
    is_anonymous: Incomplete
    can_manage_chat: Incomplete
    can_delete_messages: Incomplete
    can_manage_video_chats: Incomplete
    can_restrict_members: Incomplete
    can_promote_members: Incomplete
    can_change_info: Incomplete
    can_invite_users: Incomplete
    can_post_messages: Incomplete
    can_edit_messages: Incomplete
    can_pin_messages: Incomplete
    can_manage_topics: Incomplete
    can_post_stories: Incomplete
    can_edit_stories: Incomplete
    can_delete_stories: Incomplete
    def __init__(self, is_anonymous: bool, can_manage_chat: bool, can_delete_messages: bool, can_manage_video_chats: bool, can_restrict_members: bool, can_promote_members: bool, can_change_info: bool, can_invite_users: bool, can_post_messages: bool = ..., can_edit_messages: bool = ..., can_pin_messages: bool = ..., can_manage_topics: bool = ..., can_post_stories: bool = ..., can_edit_stories: bool = ..., can_delete_stories: bool = ...) -> None: ...
    def to_dict(self): ...
    def to_json(self): ...

class InputFile:
    def __init__(self, file) -> None: ...
    @property
    def file(self): ...

class ForumTopicCreated(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    name: Incomplete
    icon_color: Incomplete
    icon_custom_emoji_id: Incomplete
    def __init__(self, name: str, icon_color: int, icon_custom_emoji_id: Optional[str] = ...) -> None: ...

class ForumTopicClosed(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    def __init__(self) -> None: ...

class ForumTopicReopened(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    def __init__(self) -> None: ...

class ForumTopicEdited(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    name: Incomplete
    icon_custom_emoji_id: Incomplete
    def __init__(self, name: Optional[str] = ..., icon_custom_emoji_id: Optional[str] = ...) -> None: ...

class GeneralForumTopicHidden(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    def __init__(self) -> None: ...

class GeneralForumTopicUnhidden(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    def __init__(self) -> None: ...

class ForumTopic(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    message_thread_id: Incomplete
    name: Incomplete
    icon_color: Incomplete
    icon_custom_emoji_id: Incomplete
    def __init__(self, message_thread_id: int, name: str, icon_color: int, icon_custom_emoji_id: Optional[str] = ...) -> None: ...

class WriteAccessAllowed(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    web_app_name: Incomplete
    from_request: Incomplete
    from_attachment_menu: Incomplete
    def __init__(self, from_request: Optional[bool] = ..., web_app_name: Optional[str] = ..., from_attachment_menu: Optional[bool] = ...) -> None: ...

class UserShared(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    request_id: Incomplete
    user_id: Incomplete
    def __init__(self, request_id: int, user_id: int) -> None: ...

class ChatShared(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    request_id: Incomplete
    chat_id: Incomplete
    def __init__(self, request_id: int, chat_id: int) -> None: ...

class BotDescription(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    description: Incomplete
    def __init__(self, description: str) -> None: ...

class BotShortDescription(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    short_description: Incomplete
    def __init__(self, short_description: str) -> None: ...

class InputSticker(Dictionaryable, JsonSerializable):
    sticker: Incomplete
    emoji_list: Incomplete
    mask_position: Incomplete
    keywords: Incomplete
    def __init__(self, sticker: Union[str, InputFile], emoji_list: List[str], mask_position: Optional[MaskPosition] = ..., keywords: Optional[List[str]] = ...) -> None: ...
    def to_dict(self) -> dict: ...
    def to_json(self) -> str: ...
    def convert_input_sticker(self): ...

class SwitchInlineQueryChosenChat(JsonDeserializable, Dictionaryable, JsonSerializable):
    @classmethod
    def de_json(cls, json_string): ...
    query: Incomplete
    allow_user_chats: Incomplete
    allow_bot_chats: Incomplete
    allow_group_chats: Incomplete
    allow_channel_chats: Incomplete
    def __init__(self, query: Incomplete | None = ..., allow_user_chats: Incomplete | None = ..., allow_bot_chats: Incomplete | None = ..., allow_group_chats: Incomplete | None = ..., allow_channel_chats: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...
    def to_json(self): ...

class BotName(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    name: Incomplete
    def __init__(self, name: str) -> None: ...

class InlineQueryResultsButton(JsonSerializable, Dictionaryable):
    text: Incomplete
    web_app: Incomplete
    start_parameter: Incomplete
    def __init__(self, text: str, web_app: Optional[WebAppInfo] = ..., start_parameter: Optional[str] = ...) -> None: ...
    def to_dict(self) -> dict: ...
    def to_json(self) -> str: ...

class Story(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string): ...
    def __init__(self) -> None: ...
