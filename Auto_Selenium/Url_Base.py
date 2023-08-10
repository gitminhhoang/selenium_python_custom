

BASE_URL = "http://127.0.0.1:5555/"

OPEN_PROFILE = BASE_URL+ "openProfile?uuid={uuid}"
CLOSE_PROFILE = BASE_URL+ "closeProfile?uuid={uuid}"
CHECKING_PROFILE = BASE_URL+ "authorize?uuid={uuid}"
GET_LIST_PROFILE =  BASE_URL+ "profileList?page={page}&limit={limit}"
GET_LIST_CONFIG_DEFAULT =  BASE_URL+ "get-list-config-default?page={page}&limit={limit}"
GET_LIST_STATUS =  BASE_URL+ "get-list-status"
GET_LIST_TAG = BASE_URL+  "get-list-tag"
GET_PROFILE_BY_UUID = BASE_URL+  "browser/get-profile-by-uuid?uuid={uuid}"
CREATE_PROFILE_DEFAULT =  BASE_URL+ "create-profile-by-default"
CREATE_PROFILE_CUSTOMIZE = BASE_URL+  "create-profile-custom"
UPDATE_NOTE =  BASE_URL+ "browser/update-note"
UPDATE_NAME =  BASE_URL+ "browser/update-name"
SYNC_TAG =  BASE_URL+ "sync-tags"
CHANGE_STATUS =  BASE_URL+ "change-status"
DELETE_PROFILE =  BASE_URL+ "delete-profile"
UPDATE_PROXY =  BASE_URL+ "update-proxy"
UPDATE_PROXY_PROFILE = BASE_URL+  "update-proxy-profile"
