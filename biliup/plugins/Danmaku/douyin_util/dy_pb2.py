# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x64y.proto\x12\x0b\x64ouyin_util\"\xee\x02\n\x08Response\x12*\n\x0cmessagesList\x18\x01 \x03(\x0b\x32\x14.douyin_util.Message\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\t\x12\x15\n\rfetchInterval\x18\x03 \x01(\x04\x12\x0b\n\x03now\x18\x04 \x01(\x04\x12\x13\n\x0binternalExt\x18\x05 \x01(\t\x12\x11\n\tfetchType\x18\x06 \x01(\r\x12;\n\x0brouteParams\x18\x07 \x03(\x0b\x32&.douyin_util.Response.RouteParamsEntry\x12\x19\n\x11heartbeatDuration\x18\x08 \x01(\x04\x12\x0f\n\x07needAck\x18\t \x01(\x08\x12\x12\n\npushServer\x18\n \x01(\t\x12\x12\n\nliveCursor\x18\x0b \x01(\t\x12\x15\n\rhistoryNoMore\x18\x0c \x01(\x08\x1a\x32\n\x10RouteParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9a\x01\n\x07Message\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\r\n\x05msgId\x18\x03 \x01(\x03\x12\x0f\n\x07msgType\x18\x04 \x01(\x05\x12\x0e\n\x06offset\x18\x05 \x01(\x03\x12\x15\n\rneedWrdsStore\x18\x06 \x01(\x08\x12\x13\n\x0bwrdsVersion\x18\x07 \x01(\x03\x12\x12\n\nwrdsSubKey\x18\x08 \x01(\t\"\xf2\x04\n\x0b\x43hatMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12\x1f\n\x04user\x18\x02 \x01(\x0b\x32\x11.douyin_util.User\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x17\n\x0fvisibleToSender\x18\x04 \x01(\x08\x12+\n\x0f\x62\x61\x63kgroundImage\x18\x05 \x01(\x0b\x32\x12.douyin_util.Image\x12\x1b\n\x13\x66ullScreenTextColor\x18\x06 \x01(\t\x12-\n\x11\x62\x61\x63kgroundImageV2\x18\x07 \x01(\x0b\x32\x12.douyin_util.Image\x12\x37\n\x10publicAreaCommon\x18\x08 \x01(\x0b\x32\x1d.douyin_util.PublicAreaCommon\x12%\n\tgiftImage\x18\t \x01(\x0b\x32\x12.douyin_util.Image\x12\x12\n\nagreeMsgId\x18\x0b \x01(\x04\x12\x15\n\rpriorityLevel\x18\x0c \x01(\r\x12=\n\x13landscapeAreaCommon\x18\r \x01(\x0b\x32 .douyin_util.LandscapeAreaCommon\x12\x11\n\teventTime\x18\x0f \x01(\x04\x12\x12\n\nsendReview\x18\x10 \x01(\x08\x12\x14\n\x0c\x66romIntercom\x18\x11 \x01(\x08\x12\x1c\n\x14intercomHideUserCard\x18\x12 \x01(\x08\x12\x0e\n\x06\x63hatBy\x18\x14 \x01(\t\x12\x1e\n\x16individualChatPriority\x18\x15 \x01(\r\x12%\n\nrtfContent\x18\x16 \x01(\x0b\x32\x11.douyin_util.Text\"\xa6\x01\n\x13LandscapeAreaCommon\x12\x10\n\x08showHead\x18\x01 \x01(\x08\x12\x14\n\x0cshowNickname\x18\x02 \x01(\x08\x12\x15\n\rshowFontColor\x18\x03 \x01(\x08\x12\x16\n\x0e\x63olorValueList\x18\x04 \x03(\t\x12\x38\n\x13\x63ommentTypeTagsList\x18\x05 \x03(\x0e\x32\x1b.douyin_util.CommentTypeTag\"\x96\x03\n\x12RoomUserSeqMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12=\n\tranksList\x18\x02 \x03(\x0b\x32*.douyin_util.RoomUserSeqMessageContributor\x12\r\n\x05total\x18\x03 \x01(\x03\x12\x0e\n\x06popStr\x18\x04 \x01(\t\x12=\n\tseatsList\x18\x05 \x03(\x0b\x32*.douyin_util.RoomUserSeqMessageContributor\x12\x12\n\npopularity\x18\x06 \x01(\x03\x12\x11\n\ttotalUser\x18\x07 \x01(\x03\x12\x14\n\x0ctotalUserStr\x18\x08 \x01(\t\x12\x10\n\x08totalStr\x18\t \x01(\t\x12\x1b\n\x13onlineUserForAnchor\x18\n \x01(\t\x12\x18\n\x10totalPvForAnchor\x18\x0b \x01(\t\x12\x17\n\x0fupRightStatsStr\x18\x0c \x01(\t\x12\x1f\n\x17upRightStatsStrComplete\x18\r \x01(\t\"h\n\x11\x43ommonTextMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12\x1f\n\x04user\x18\x02 \x01(\x0b\x32\x11.douyin_util.User\x12\r\n\x05scene\x18\x03 \x01(\t\"\x8e\x01\n\x16UpdateFanTicketMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12\x1e\n\x16roomFanTicketCountText\x18\x02 \x01(\t\x12\x1a\n\x12roomFanTicketCount\x18\x03 \x01(\x04\x12\x13\n\x0b\x66orceUpdate\x18\x04 \x01(\x08\"\xae\x01\n\x1dRoomUserSeqMessageContributor\x12\r\n\x05score\x18\x01 \x01(\x04\x12\x1f\n\x04user\x18\x02 \x01(\x0b\x32\x11.douyin_util.User\x12\x0c\n\x04rank\x18\x03 \x01(\x04\x12\r\n\x05\x64\x65lta\x18\x04 \x01(\x04\x12\x10\n\x08isHidden\x18\x05 \x01(\x08\x12\x18\n\x10scoreDescription\x18\x06 \x01(\t\x12\x14\n\x0c\x65xactlyScore\x18\x07 \x01(\t\"\xd9\x06\n\x0bGiftMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12\x0e\n\x06giftId\x18\x02 \x01(\x04\x12\x16\n\x0e\x66\x61nTicketCount\x18\x03 \x01(\x04\x12\x12\n\ngroupCount\x18\x04 \x01(\x04\x12\x13\n\x0brepeatCount\x18\x05 \x01(\x04\x12\x12\n\ncomboCount\x18\x06 \x01(\x04\x12\x1f\n\x04user\x18\x07 \x01(\x0b\x32\x11.douyin_util.User\x12!\n\x06toUser\x18\x08 \x01(\x0b\x32\x11.douyin_util.User\x12\x11\n\trepeatEnd\x18\t \x01(\r\x12+\n\ntextEffect\x18\n \x01(\x0b\x32\x17.douyin_util.TextEffect\x12\x0f\n\x07groupId\x18\x0b \x01(\x04\x12\x17\n\x0fincomeTaskgifts\x18\x0c \x01(\x04\x12\x1a\n\x12roomFanTicketCount\x18\r \x01(\x04\x12-\n\x08priority\x18\x0e \x01(\x0b\x32\x1b.douyin_util.GiftIMPriority\x12%\n\x04gift\x18\x0f \x01(\x0b\x32\x17.douyin_util.GiftStruct\x12\r\n\x05logId\x18\x10 \x01(\t\x12\x10\n\x08sendType\x18\x11 \x01(\x04\x12\x37\n\x10publicAreaCommon\x18\x12 \x01(\x0b\x32\x1d.douyin_util.PublicAreaCommon\x12*\n\x0ftrayDisplayText\x18\x13 \x01(\x0b\x32\x11.douyin_util.Text\x12\x1c\n\x14\x62\x61nnedDisplayEffects\x18\x14 \x01(\x04\x12\x16\n\x0e\x64isplayForSelf\x18\x19 \x01(\x08\x12\x18\n\x10interactGiftInfo\x18\x1a \x01(\t\x12\x13\n\x0b\x64iyItemInfo\x18\x1b \x01(\t\x12\x17\n\x0fminAssetSetList\x18\x1c \x03(\x04\x12\x12\n\ntotalCount\x18\x1d \x01(\x04\x12\x18\n\x10\x63lientGiftSource\x18\x1e \x01(\r\x12\x15\n\rtoUserIdsList\x18  \x03(\x04\x12\x10\n\x08sendTime\x18! \x01(\x04\x12\x1b\n\x13\x66orceDisplayEffects\x18\" \x01(\x04\x12\x0f\n\x07traceId\x18# \x01(\t\x12\x17\n\x0f\x65\x66\x66\x65\x63tDisplayTs\x18$ \x01(\x04\"\xb2\x03\n\nGiftStruct\x12!\n\x05image\x18\x01 \x01(\x0b\x32\x12.douyin_util.Image\x12\x10\n\x08\x64\x65scribe\x18\x02 \x01(\t\x12\x0e\n\x06notify\x18\x03 \x01(\x08\x12\x10\n\x08\x64uration\x18\x04 \x01(\x04\x12\n\n\x02id\x18\x05 \x01(\x04\x12\x12\n\nforLinkmic\x18\x07 \x01(\x08\x12\x0e\n\x06\x64oodle\x18\x08 \x01(\x08\x12\x13\n\x0b\x66orFansclub\x18\t \x01(\x08\x12\r\n\x05\x63ombo\x18\n \x01(\x08\x12\x0c\n\x04type\x18\x0b \x01(\r\x12\x14\n\x0c\x64iamondCount\x18\x0c \x01(\r\x12\x1a\n\x12isDisplayedOnPanel\x18\r \x01(\x08\x12\x17\n\x0fprimaryEffectId\x18\x0e \x01(\x04\x12)\n\rgiftLabelIcon\x18\x0f \x01(\x0b\x32\x12.douyin_util.Image\x12\x0c\n\x04name\x18\x10 \x01(\t\x12\x0e\n\x06region\x18\x11 \x01(\t\x12\x0e\n\x06manual\x18\x12 \x01(\t\x12\x11\n\tforCustom\x18\x13 \x01(\x08\x12 \n\x04icon\x18\x15 \x01(\x0b\x32\x12.douyin_util.Image\x12\x12\n\nactionType\x18\x16 \x01(\r\"U\n\x0eGiftIMPriority\x12\x16\n\x0equeueSizesList\x18\x01 \x03(\x04\x12\x19\n\x11selfQueuePriority\x18\x02 \x01(\x04\x12\x10\n\x08priority\x18\x03 \x01(\x04\"o\n\nTextEffect\x12/\n\x08portrait\x18\x01 \x01(\x0b\x32\x1d.douyin_util.TextEffectDetail\x12\x30\n\tlandscape\x18\x02 \x01(\x0b\x32\x1d.douyin_util.TextEffectDetail\"\xc0\x02\n\x10TextEffectDetail\x12\x1f\n\x04text\x18\x01 \x01(\x0b\x32\x11.douyin_util.Text\x12\x14\n\x0ctextFontSize\x18\x02 \x01(\r\x12&\n\nbackground\x18\x03 \x01(\x0b\x32\x12.douyin_util.Image\x12\r\n\x05start\x18\x04 \x01(\r\x12\x10\n\x08\x64uration\x18\x05 \x01(\r\x12\t\n\x01x\x18\x06 \x01(\r\x12\t\n\x01y\x18\x07 \x01(\r\x12\r\n\x05width\x18\x08 \x01(\r\x12\x0e\n\x06height\x18\t \x01(\r\x12\x10\n\x08shadowDx\x18\n \x01(\r\x12\x10\n\x08shadowDy\x18\x0b \x01(\r\x12\x14\n\x0cshadowRadius\x18\x0c \x01(\r\x12\x13\n\x0bshadowColor\x18\r \x01(\t\x12\x13\n\x0bstrokeColor\x18\x0e \x01(\t\x12\x13\n\x0bstrokeWidth\x18\x0f \x01(\r\"\x9c\x05\n\rMemberMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12\x1f\n\x04user\x18\x02 \x01(\x0b\x32\x11.douyin_util.User\x12\x13\n\x0bmemberCount\x18\x03 \x01(\x04\x12#\n\x08operator\x18\x04 \x01(\x0b\x32\x11.douyin_util.User\x12\x14\n\x0cisSetToAdmin\x18\x05 \x01(\x08\x12\x11\n\tisTopUser\x18\x06 \x01(\x08\x12\x11\n\trankScore\x18\x07 \x01(\x04\x12\x11\n\ttopUserNo\x18\x08 \x01(\x04\x12\x11\n\tenterType\x18\t \x01(\x04\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\x04\x12\x19\n\x11\x61\x63tionDescription\x18\x0b \x01(\t\x12\x0e\n\x06userId\x18\x0c \x01(\x04\x12/\n\x0c\x65\x66\x66\x65\x63tConfig\x18\r \x01(\x0b\x32\x19.douyin_util.EffectConfig\x12\x0e\n\x06popStr\x18\x0e \x01(\t\x12\x34\n\x11\x65nterEffectConfig\x18\x0f \x01(\x0b\x32\x19.douyin_util.EffectConfig\x12+\n\x0f\x62\x61\x63kgroundImage\x18\x10 \x01(\x0b\x32\x12.douyin_util.Image\x12-\n\x11\x62\x61\x63kgroundImageV2\x18\x11 \x01(\x0b\x32\x12.douyin_util.Image\x12,\n\x11\x61nchorDisplayText\x18\x12 \x01(\x0b\x32\x11.douyin_util.Text\x12\x37\n\x10publicAreaCommon\x18\x13 \x01(\x0b\x32\x1d.douyin_util.PublicAreaCommon\x12\x18\n\x10userEnterTipType\x18\x14 \x01(\x04\x12\x1a\n\x12\x61nchorEnterTipType\x18\x15 \x01(\x04\"s\n\x10PublicAreaCommon\x12%\n\tuserLabel\x18\x01 \x01(\x0b\x32\x12.douyin_util.Image\x12\x19\n\x11userConsumeInRoom\x18\x02 \x01(\x04\x12\x1d\n\x15userSendGiftCntInRoom\x18\x03 \x01(\x04\"\xbe\x05\n\x0c\x45\x66\x66\x65\x63tConfig\x12\x0c\n\x04type\x18\x01 \x01(\x04\x12 \n\x04icon\x18\x02 \x01(\x0b\x32\x12.douyin_util.Image\x12\x11\n\tavatarPos\x18\x03 \x01(\x04\x12\x1f\n\x04text\x18\x04 \x01(\x0b\x32\x11.douyin_util.Text\x12$\n\x08textIcon\x18\x05 \x01(\x0b\x32\x12.douyin_util.Image\x12\x10\n\x08stayTime\x18\x06 \x01(\r\x12\x13\n\x0b\x61nimAssetId\x18\x07 \x01(\x04\x12!\n\x05\x62\x61\x64ge\x18\x08 \x01(\x0b\x32\x12.douyin_util.Image\x12\x1c\n\x14\x66lexSettingArrayList\x18\t \x03(\x04\x12+\n\x0ftextIconOverlay\x18\n \x01(\x0b\x32\x12.douyin_util.Image\x12)\n\ranimatedBadge\x18\x0b \x01(\x0b\x32\x12.douyin_util.Image\x12\x15\n\rhasSweepLight\x18\x0c \x01(\x08\x12 \n\x18textFlexSettingArrayList\x18\r \x03(\x04\x12\x19\n\x11\x63\x65nterAnimAssetId\x18\x0e \x01(\x04\x12(\n\x0c\x64ynamicImage\x18\x0f \x01(\x0b\x32\x12.douyin_util.Image\x12\x39\n\x08\x65xtraMap\x18\x10 \x03(\x0b\x32\'.douyin_util.EffectConfig.ExtraMapEntry\x12\x16\n\x0emp4AnimAssetId\x18\x11 \x01(\x04\x12\x10\n\x08priority\x18\x12 \x01(\x04\x12\x13\n\x0bmaxWaitTime\x18\x13 \x01(\x04\x12\x0f\n\x07\x64ressId\x18\x14 \x01(\t\x12\x11\n\talignment\x18\x15 \x01(\x04\x12\x17\n\x0f\x61lignmentOffset\x18\x16 \x01(\x04\x1a/\n\rExtraMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x86\x01\n\x04Text\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\rdefaultPatter\x18\x02 \x01(\t\x12.\n\rdefaultFormat\x18\x03 \x01(\x0b\x32\x17.douyin_util.TextFormat\x12*\n\npiecesList\x18\x04 \x03(\x0b\x32\x16.douyin_util.TextPiece\"\xd2\x02\n\tTextPiece\x12\x0c\n\x04type\x18\x01 \x01(\x08\x12\'\n\x06\x66ormat\x18\x02 \x01(\x0b\x32\x17.douyin_util.TextFormat\x12\x13\n\x0bstringValue\x18\x03 \x01(\t\x12-\n\tuserValue\x18\x04 \x01(\x0b\x32\x1a.douyin_util.TextPieceUser\x12-\n\tgiftValue\x18\x05 \x01(\x0b\x32\x1a.douyin_util.TextPieceGift\x12/\n\nheartValue\x18\x06 \x01(\x0b\x32\x1b.douyin_util.TextPieceHeart\x12\x39\n\x0fpatternRefValue\x18\x07 \x01(\x0b\x32 .douyin_util.TextPiecePatternRef\x12/\n\nimageValue\x18\x08 \x01(\x0b\x32\x1b.douyin_util.TextPieceImage\"H\n\x0eTextPieceImage\x12!\n\x05image\x18\x01 \x01(\x0b\x32\x12.douyin_util.Image\x12\x13\n\x0bscalingRate\x18\x02 \x01(\x02\":\n\x13TextPiecePatternRef\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65\x66\x61ultPattern\x18\x02 \x01(\t\"\x1f\n\x0eTextPieceHeart\x12\r\n\x05\x63olor\x18\x01 \x01(\t\"I\n\rTextPieceGift\x12\x0e\n\x06giftId\x18\x01 \x01(\x04\x12(\n\x07nameRef\x18\x02 \x01(\x0b\x32\x17.douyin_util.PatternRef\"1\n\nPatternRef\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65\x66\x61ultPattern\x18\x02 \x01(\t\"C\n\rTextPieceUser\x12\x1f\n\x04user\x18\x01 \x01(\x0b\x32\x11.douyin_util.User\x12\x11\n\twithColon\x18\x02 \x01(\x08\"\xa3\x01\n\nTextFormat\x12\r\n\x05\x63olor\x18\x01 \x01(\t\x12\x0c\n\x04\x62old\x18\x02 \x01(\x08\x12\x0e\n\x06italic\x18\x03 \x01(\x08\x12\x0e\n\x06weight\x18\x04 \x01(\r\x12\x13\n\x0bitalicAngle\x18\x05 \x01(\r\x12\x10\n\x08\x66ontSize\x18\x06 \x01(\r\x12\x1a\n\x12useHeighLightColor\x18\x07 \x01(\x08\x12\x15\n\ruseRemoteClor\x18\x08 \x01(\x08\"\xe3\x02\n\x0bLikeMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\x12\r\n\x05total\x18\x03 \x01(\x04\x12\r\n\x05\x63olor\x18\x04 \x01(\x04\x12\x1f\n\x04user\x18\x05 \x01(\x0b\x32\x11.douyin_util.User\x12\x0c\n\x04icon\x18\x06 \x01(\t\x12\x37\n\x10\x64oubleLikeDetail\x18\x07 \x01(\x0b\x32\x1d.douyin_util.DoubleLikeDetail\x12;\n\x12\x64isplayControlInfo\x18\x08 \x01(\x0b\x32\x1f.douyin_util.DisplayControlInfo\x12\x17\n\x0flinkmicGuestUid\x18\t \x01(\x04\x12\r\n\x05scene\x18\n \x01(\t\x12\x35\n\x0fpicoDisplayInfo\x18\x0b \x01(\x0b\x32\x1c.douyin_util.PicoDisplayInfo\"\xdb\x01\n\rSocialMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12\x1f\n\x04user\x18\x02 \x01(\x0b\x32\x11.douyin_util.User\x12\x11\n\tshareType\x18\x03 \x01(\x04\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\x04\x12\x13\n\x0bshareTarget\x18\x05 \x01(\t\x12\x13\n\x0b\x66ollowCount\x18\x06 \x01(\x04\x12\x37\n\x10publicAreaCommon\x18\x07 \x01(\x0b\x32\x1d.douyin_util.PublicAreaCommon\"q\n\x0fPicoDisplayInfo\x12\x15\n\rcomboSumCount\x18\x01 \x01(\x04\x12\r\n\x05\x65moji\x18\x02 \x01(\t\x12%\n\temojiIcon\x18\x03 \x01(\x0b\x32\x12.douyin_util.Image\x12\x11\n\temojiText\x18\x04 \x01(\t\"_\n\x10\x44oubleLikeDetail\x12\x12\n\ndoubleFlag\x18\x01 \x01(\x08\x12\r\n\x05seqId\x18\x02 \x01(\r\x12\x13\n\x0brenewalsNum\x18\x03 \x01(\r\x12\x13\n\x0btriggersNum\x18\x04 \x01(\r\"9\n\x12\x44isplayControlInfo\x12\x10\n\x08showText\x18\x01 \x01(\x08\x12\x11\n\tshowIcons\x18\x02 \x01(\x08\"\xd7\x01\n\x12\x45pisodeChatMessage\x12$\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x14.douyin_util.Message\x12\x1f\n\x04user\x18\x02 \x01(\x0b\x32\x11.douyin_util.User\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x16\n\x0evisibleToSende\x18\x04 \x01(\x08\x12%\n\tgiftImage\x18\x07 \x01(\x0b\x32\x12.douyin_util.Image\x12\x12\n\nagreeMsgId\x18\x08 \x01(\x04\x12\x16\n\x0e\x63olorValueList\x18\t \x03(\t\"\x92\x01\n\x18MatchAgainstScoreMessage\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.douyin_util.Common\x12%\n\x07\x61gainst\x18\x02 \x01(\x0b\x32\x14.douyin_util.Against\x12\x13\n\x0bmatchStatus\x18\x03 \x01(\r\x12\x15\n\rdisplayStatus\x18\x04 \x01(\r\"\x9c\x03\n\x07\x41gainst\x12\x10\n\x08leftName\x18\x01 \x01(\t\x12$\n\x08leftLogo\x18\x02 \x01(\x0b\x32\x12.douyin_util.Image\x12\x10\n\x08leftGoal\x18\x03 \x01(\t\x12\x11\n\trightName\x18\x06 \x01(\t\x12%\n\trightLogo\x18\x07 \x01(\x0b\x32\x12.douyin_util.Image\x12\x11\n\trightGoal\x18\x08 \x01(\t\x12\x11\n\ttimestamp\x18\x0b \x01(\x04\x12\x0f\n\x07version\x18\x0c \x01(\x04\x12\x12\n\nleftTeamId\x18\r \x01(\x04\x12\x13\n\x0brightTeamId\x18\x0e \x01(\x04\x12\x19\n\x11\x64iffSei2absSecond\x18\x0f \x01(\x04\x12\x16\n\x0e\x66inalGoalStage\x18\x10 \x01(\r\x12\x18\n\x10\x63urrentGoalStage\x18\x11 \x01(\r\x12\x19\n\x11leftScoreAddition\x18\x12 \x01(\r\x12\x1a\n\x12rightScoreAddition\x18\x13 \x01(\r\x12\x13\n\x0bleftGoalInt\x18\x14 \x01(\x04\x12\x14\n\x0crightGoalInt\x18\x15 \x01(\x04\"\xd6\x03\n\x06\x43ommon\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\r\n\x05msgId\x18\x02 \x01(\x04\x12\x0e\n\x06roomId\x18\x03 \x01(\x04\x12\x12\n\ncreateTime\x18\x04 \x01(\x04\x12\x0f\n\x07monitor\x18\x05 \x01(\r\x12\x11\n\tisShowMsg\x18\x06 \x01(\x08\x12\x10\n\x08\x64\x65scribe\x18\x07 \x01(\t\x12\x10\n\x08\x66oldType\x18\t \x01(\x04\x12\x16\n\x0e\x61nchorFoldType\x18\n \x01(\x04\x12\x15\n\rpriorityScore\x18\x0b \x01(\x04\x12\r\n\x05logId\x18\x0c \x01(\t\x12\x19\n\x11msgProcessFilterK\x18\r \x01(\t\x12\x19\n\x11msgProcessFilterV\x18\x0e \x01(\t\x12\x1f\n\x04user\x18\x0f \x01(\x0b\x32\x11.douyin_util.User\x12\x18\n\x10\x61nchorFoldTypeV2\x18\x11 \x01(\x04\x12\x1a\n\x12processAtSeiTimeMs\x18\x12 \x01(\x04\x12\x18\n\x10randomDispatchMs\x18\x13 \x01(\x04\x12\x12\n\nisDispatch\x18\x14 \x01(\x08\x12\x11\n\tchannelId\x18\x15 \x01(\x04\x12\x19\n\x11\x64iffSei2absSecond\x18\x16 \x01(\x04\x12\x1a\n\x12\x61nchorFoldDuration\x18\x17 \x01(\x04\"\xf3\x04\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07shortId\x18\x02 \x01(\x04\x12\x10\n\x08nickName\x18\x03 \x01(\t\x12\x0e\n\x06gender\x18\x04 \x01(\r\x12\x11\n\tSignature\x18\x05 \x01(\t\x12\r\n\x05Level\x18\x06 \x01(\r\x12\x10\n\x08\x42irthday\x18\x07 \x01(\x04\x12\x11\n\tTelephone\x18\x08 \x01(\t\x12\'\n\x0b\x41vatarThumb\x18\t \x01(\x0b\x32\x12.douyin_util.Image\x12(\n\x0c\x41vatarMedium\x18\n \x01(\x0b\x32\x12.douyin_util.Image\x12\'\n\x0b\x41vatarLarge\x18\x0b \x01(\x0b\x32\x12.douyin_util.Image\x12\x10\n\x08Verified\x18\x0c \x01(\x08\x12\x12\n\nExperience\x18\r \x01(\r\x12\x0c\n\x04\x63ity\x18\x0e \x01(\t\x12\x0e\n\x06Status\x18\x0f \x01(\x05\x12\x12\n\nCreateTime\x18\x10 \x01(\x04\x12\x12\n\nModifyTime\x18\x11 \x01(\x04\x12\x0e\n\x06Secret\x18\x12 \x01(\r\x12\x16\n\x0eShareQrcodeUri\x18\x13 \x01(\t\x12\x1a\n\x12IncomeSharePercent\x18\x14 \x01(\r\x12*\n\x0e\x42\x61\x64geImageList\x18\x15 \x03(\x0b\x32\x12.douyin_util.Image\x12\x11\n\tSpecialId\x18\x1a \x01(\t\x12(\n\x0c\x41vatarBorder\x18\x1b \x01(\x0b\x32\x12.douyin_util.Image\x12!\n\x05Medal\x18\x1c \x01(\x0b\x32\x12.douyin_util.Image\x12-\n\x11RealTimeIconsList\x18\x1d \x03(\x0b\x32\x12.douyin_util.Image\"\xb1\x02\n\x05Image\x12\x13\n\x0burlListList\x18\x01 \x03(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\r\n\x05width\x18\x04 \x01(\x04\x12\x10\n\x08\x61vgColor\x18\x05 \x01(\t\x12\x11\n\timageType\x18\x06 \x01(\r\x12\x12\n\nopenWebUrl\x18\x07 \x01(\t\x12*\n\x07\x63ontent\x18\x08 \x01(\x0b\x32\x19.douyin_util.ImageContent\x12\x12\n\nisAnimated\x18\t \x01(\x08\x12\x36\n\x0f\x46lexSettingList\x18\n \x01(\x0b\x32\x1d.douyin_util.NinePatchSetting\x12\x36\n\x0fTextSettingList\x18\x0b \x01(\x0b\x32\x1d.douyin_util.NinePatchSetting\"+\n\x10NinePatchSetting\x12\x17\n\x0fsettingListList\x18\x01 \x03(\t\"W\n\x0cImageContent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tfontColor\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x04\x12\x17\n\x0f\x61lternativeText\x18\x04 \x01(\t\"\xb8\x01\n\tPushFrame\x12\r\n\x05seqId\x18\x01 \x01(\x04\x12\r\n\x05logId\x18\x02 \x01(\x04\x12\x0f\n\x07service\x18\x03 \x01(\x04\x12\x0e\n\x06method\x18\x04 \x01(\x04\x12-\n\x0bheadersList\x18\x05 \x03(\x0b\x32\x18.douyin_util.HeadersList\x12\x17\n\x0fpayloadEncoding\x18\x06 \x01(\t\x12\x13\n\x0bpayloadType\x18\x07 \x01(\t\x12\x0f\n\x07payload\x18\x08 \x01(\x0c\")\n\x0bHeadersList\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t*C\n\x0e\x43ommentTypeTag\x12\x19\n\x15\x43OMMENTTYPETAGUNKNOWN\x10\x00\x12\x16\n\x12\x43OMMENTTYPETAGSTAR\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESPONSE_ROUTEPARAMSENTRY._options = None
  _RESPONSE_ROUTEPARAMSENTRY._serialized_options = b'8\001'
  _EFFECTCONFIG_EXTRAMAPENTRY._options = None
  _EFFECTCONFIG_EXTRAMAPENTRY._serialized_options = b'8\001'
  _globals['_COMMENTTYPETAG']._serialized_start=9913
  _globals['_COMMENTTYPETAG']._serialized_end=9980
  _globals['_RESPONSE']._serialized_start=26
  _globals['_RESPONSE']._serialized_end=392
  _globals['_RESPONSE_ROUTEPARAMSENTRY']._serialized_start=342
  _globals['_RESPONSE_ROUTEPARAMSENTRY']._serialized_end=392
  _globals['_MESSAGE']._serialized_start=395
  _globals['_MESSAGE']._serialized_end=549
  _globals['_CHATMESSAGE']._serialized_start=552
  _globals['_CHATMESSAGE']._serialized_end=1178
  _globals['_LANDSCAPEAREACOMMON']._serialized_start=1181
  _globals['_LANDSCAPEAREACOMMON']._serialized_end=1347
  _globals['_ROOMUSERSEQMESSAGE']._serialized_start=1350
  _globals['_ROOMUSERSEQMESSAGE']._serialized_end=1756
  _globals['_COMMONTEXTMESSAGE']._serialized_start=1758
  _globals['_COMMONTEXTMESSAGE']._serialized_end=1862
  _globals['_UPDATEFANTICKETMESSAGE']._serialized_start=1865
  _globals['_UPDATEFANTICKETMESSAGE']._serialized_end=2007
  _globals['_ROOMUSERSEQMESSAGECONTRIBUTOR']._serialized_start=2010
  _globals['_ROOMUSERSEQMESSAGECONTRIBUTOR']._serialized_end=2184
  _globals['_GIFTMESSAGE']._serialized_start=2187
  _globals['_GIFTMESSAGE']._serialized_end=3044
  _globals['_GIFTSTRUCT']._serialized_start=3047
  _globals['_GIFTSTRUCT']._serialized_end=3481
  _globals['_GIFTIMPRIORITY']._serialized_start=3483
  _globals['_GIFTIMPRIORITY']._serialized_end=3568
  _globals['_TEXTEFFECT']._serialized_start=3570
  _globals['_TEXTEFFECT']._serialized_end=3681
  _globals['_TEXTEFFECTDETAIL']._serialized_start=3684
  _globals['_TEXTEFFECTDETAIL']._serialized_end=4004
  _globals['_MEMBERMESSAGE']._serialized_start=4007
  _globals['_MEMBERMESSAGE']._serialized_end=4675
  _globals['_PUBLICAREACOMMON']._serialized_start=4677
  _globals['_PUBLICAREACOMMON']._serialized_end=4792
  _globals['_EFFECTCONFIG']._serialized_start=4795
  _globals['_EFFECTCONFIG']._serialized_end=5497
  _globals['_EFFECTCONFIG_EXTRAMAPENTRY']._serialized_start=5450
  _globals['_EFFECTCONFIG_EXTRAMAPENTRY']._serialized_end=5497
  _globals['_TEXT']._serialized_start=5500
  _globals['_TEXT']._serialized_end=5634
  _globals['_TEXTPIECE']._serialized_start=5637
  _globals['_TEXTPIECE']._serialized_end=5975
  _globals['_TEXTPIECEIMAGE']._serialized_start=5977
  _globals['_TEXTPIECEIMAGE']._serialized_end=6049
  _globals['_TEXTPIECEPATTERNREF']._serialized_start=6051
  _globals['_TEXTPIECEPATTERNREF']._serialized_end=6109
  _globals['_TEXTPIECEHEART']._serialized_start=6111
  _globals['_TEXTPIECEHEART']._serialized_end=6142
  _globals['_TEXTPIECEGIFT']._serialized_start=6144
  _globals['_TEXTPIECEGIFT']._serialized_end=6217
  _globals['_PATTERNREF']._serialized_start=6219
  _globals['_PATTERNREF']._serialized_end=6268
  _globals['_TEXTPIECEUSER']._serialized_start=6270
  _globals['_TEXTPIECEUSER']._serialized_end=6337
  _globals['_TEXTFORMAT']._serialized_start=6340
  _globals['_TEXTFORMAT']._serialized_end=6503
  _globals['_LIKEMESSAGE']._serialized_start=6506
  _globals['_LIKEMESSAGE']._serialized_end=6861
  _globals['_SOCIALMESSAGE']._serialized_start=6864
  _globals['_SOCIALMESSAGE']._serialized_end=7083
  _globals['_PICODISPLAYINFO']._serialized_start=7085
  _globals['_PICODISPLAYINFO']._serialized_end=7198
  _globals['_DOUBLELIKEDETAIL']._serialized_start=7200
  _globals['_DOUBLELIKEDETAIL']._serialized_end=7295
  _globals['_DISPLAYCONTROLINFO']._serialized_start=7297
  _globals['_DISPLAYCONTROLINFO']._serialized_end=7354
  _globals['_EPISODECHATMESSAGE']._serialized_start=7357
  _globals['_EPISODECHATMESSAGE']._serialized_end=7572
  _globals['_MATCHAGAINSTSCOREMESSAGE']._serialized_start=7575
  _globals['_MATCHAGAINSTSCOREMESSAGE']._serialized_end=7721
  _globals['_AGAINST']._serialized_start=7724
  _globals['_AGAINST']._serialized_end=8136
  _globals['_COMMON']._serialized_start=8139
  _globals['_COMMON']._serialized_end=8609
  _globals['_USER']._serialized_start=8612
  _globals['_USER']._serialized_end=9239
  _globals['_IMAGE']._serialized_start=9242
  _globals['_IMAGE']._serialized_end=9547
  _globals['_NINEPATCHSETTING']._serialized_start=9549
  _globals['_NINEPATCHSETTING']._serialized_end=9592
  _globals['_IMAGECONTENT']._serialized_start=9594
  _globals['_IMAGECONTENT']._serialized_end=9681
  _globals['_PUSHFRAME']._serialized_start=9684
  _globals['_PUSHFRAME']._serialized_end=9868
  _globals['_HEADERSLIST']._serialized_start=9870
  _globals['_HEADERSLIST']._serialized_end=9911
# @@protoc_insertion_point(module_scope)
