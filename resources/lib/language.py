from matthuisman.language import BaseLanguage

class Language(BaseLanguage):
    HIDE_CHANNEL      = 30000
    ASK_USERNAME      = 30001
    ASK_PASSWORD      = 30002
    NO_CHANNEL        = 30003
    NO_STREAM         = 30004
    ADOBE_ERROR       = 30005
    TOKEN_ERROR       = 30006
    LIVE_TV           = 30007
    RESET_HIDDEN      = 30008
    RESET_HIDDEN_OK   = 30009
    TV_SHOWS          = 30010
    MOVIES            = 30011
    SPORTS            = 30012
    BOX_SETS          = 30013
    NO_ACCESS         = 30014
    EPISODE_LABEL     = 30015
    RENEW_TOKEN_ERROR = 30016

_ = Language()