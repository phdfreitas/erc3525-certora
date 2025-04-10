TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		safe_math_narrow_bv256:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow","returnSort":{"bits":256}}
		add_noofl_256:JSON{"#class":"vc.data.TACBuiltInFunction.NoAddOverflowCheck","eName":"add_noofl","paramSorts":[{"#class":"tac.Tag.Bit256"},{"#class":"tac.Tag.Bit256"}],"returnSort":{"#class":"tac.Tag.Bool"},"tag":{"bits":256}}
		hash_2_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":2,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		skey_add:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Addition"}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
	}
	UninterpretedFunctions {
	}
	tacM0x20@1:bv256:0
	tacM0x40@1:bv256:1
	CANON11!!112:wordmap:2
	tacCodesizeCANON0:bv256:3
	tacNonce:wordmap:4
	tacCalldatabufCANON0@1:bv256:5
	tacCalldatabufCANON1@1:bool:6
	tacCalldatabufCANON2@1:bv256:7
	CANON16!!118:bv256:8
	tacM0x40!!0:bv256:1
	tacContractsCreated!!24:wordmap:9
	tacAddress!!80:bv256:10
	CANON4!!104:wordmap:11
	CANON9!!110:wordmap:12
	lastReverted:bool:13
	lastStorageCANON:wordmap:14
	CANON10!!7:wordmap:15
	CANON11!!8:wordmap:2
	CANON12!!9:wordmap:16
	CANON2!!25:wordmap:17
	tacM0x0!!173:bv256:18
	tacM0x0!!180:bv256:18
	tacM0x0!!187:bv256:18
	tacM0x0!!198:bv256:18
	tacM0x0!!205:bv256:18
	tacM0x0!!228:bv256:18
	tacM0x0!!235:bv256:18
	tacM0x0!!242:bv256:18
	tacExtcodesize!!5:wordmap:19
	CANON3!!26:wordmap:20
	CANON4!!27:wordmap:11
	tacSCANON0!!34:wordmap:21
	CANON5!!28:wordmap:22
	CANON6!!29:wordmap:23
	CANON7!!30:wordmap:24
	CANON8!!31:wordmap:25
	CANON81!20:ghostmap(bv256*bv256*bv256->bv256):26
	CANON9!!32:wordmap:12
	tacCalldatasize:bv256:27
	tacCalldatasize@1:bv256:27
	tacSCANON0!!105:wordmap:21
	CANON20!!122:wordmap:28
	CANON12!!113:wordmap:16
	tacTCANON0:wordmap:29
	tacExtcodesize!!128:wordmap:19
	CANON17!!119:bv256:30
	tacM0x0@1:bv256:18
	CANON5!!106:wordmap:22
	tacExtcodesize:wordmap:19
	CANON100:bv256:31
	CANON101:int:31
	CANON102:bv256:31
	CANON103:int:31
	CANON104:bool:31
	CANON105:bv256:31
	CANON106@1:bv256:31
	CANON107@1:bv256:31
	CANON108@1:bv256:31
	CANON109:bool:31
	CANON110@1:bv256:31
	CANON111@1:bv256:31
	CANON112:bool:31
	CANON113@1:bool:31
	CANON114@1:bv256:31
	CANON115@1:bv256:31
	CANON116:bool:31
	CANON117@1:bv256:31
	CANON118@1:bv256:31
	CANON119:bool:31
	CANON120@1:bool:31
	CANON121@1:bv256:31
	CANON122@1:bv256:31
	CANON123@1:bv256:31
	CANON124@1:bv256:31
	CANON125:bool:31
	CANON126@1:bv256:31
	CANON127@1:bv256:31
	CANON128:bool:31
	CANON129@1:bv256:31
	CANON130@1:bv256:31
	CANON131:bool:31
	CANON132:bool:31
	tacCalldatasize!!76:bv256:27
	tacMCANON0@1:bytemap:32
	tacBalance:wordmap:33
	tacMCANON0havocme30719@1:bytemap:34
	CANON21!!123:wordmap:35
	tacBalance!!87:wordmap:33
	CANON13!!114:wordmap:36
	tacNonce!!125:wordmap:4
	tacBalance!!6:wordmap:33
	lastStorageCANON1:wordmap:14
	lastStorageCANON2:wordmap:14
	lastStorageCANON3:wordmap:37
	lastStorageCANON4:wordmap:38
	lastStorageCANON5:wordmap:38
	lastStorageCANON6:wordmap:14
	lastStorageCANON7:wordmap:38
	lastStorageCANON8:wordmap:39
	lastStorageCANON9:wordmap:39
	CANON18!!120:bv256:40
	tacCalldatabuf@1:bytemap:41
	R1:bv256:3
	W4:wordmap:29
	B37:bool:31
	B38:bool:31
	B75:bool
	B90:bool:31
	B94:bool:42
	B97:bool:43
	B98:bool:43
	B99:bool:44
	I39:int
	I40:int
	I41:int
	I42:int
	I43:int
	I86:int:31
	I89:int:31
	R21:bv256:45
	R22:bv256:46
	R23:bv256:47
	R33:bv256:48
	R36:bv256:31
	R58:bv256:49
	R59:bv256:50
	R60:bv256:51
	R61:bv256:52
	R62:bv256:53
	R63:bv256:54
	R71:bv256:31
	R72:bv256
	R73:bv256
	R74:bv256:31
	R77:bv256:31
	R79:bv256:31
	R81:bv256:31
	R82:bv256:31
	R83:bv256:31
	R84:bv256:31
	R85:bv256:31
	R88:bv256:31
	R91:bv256:31
	R92:bv256:31
	R93:bv256:55
	R95:bv256:55
	R96:bv256:56
	W44:wordmap:57
	W45:wordmap:57
	W46:wordmap:57
	W47:wordmap:58
	W48:wordmap:59
	W49:wordmap:59
	W50:wordmap:57
	W51:wordmap:59
	W52:wordmap:60
	W53:wordmap:60
	W54:wordmap:57
	W55:wordmap:57
	W56:wordmap:57
	W57:wordmap:58
	W64:wordmap:57
	W65:wordmap:57
	W66:wordmap:61
	W67:wordmap
	W68:wordmap
	W69:wordmap
	W70:wordmap
	tacNonce!!2:wordmap:4
	B129:bool
	B130:bool
	B140:bool:62
	B150:bool:31
	B157:bool:31
	B161:bool:62
	B166:bool:63
	B167:bool:63
	B168:bool:64
	B179:bool:31
	B186:bool:31
	B193:bool:31
	B213:bool:31
	B217:bool:65
	B218:bool:65
	B219:bool:66
	B221:bool:31
	B222:bool:66
	B223:bool:66
	B224:bool:64
	B225:bool:64
	B226:bool:44
	B227:bool:44
	B234:bool:31
	B241:bool:31
	B248:bool:31
	B254:bool:65
	B255:bool:66
	B261:bool:63
	B262:bool:64
	B268:bool:43
	B269:bool:44
	B270:bool:67
	B271:bool:68
	B272:bool:69
	B273:bool:56
	B274:bool:70
	B275:bool:62
	R133:(uninterp) skey:56
	R134:bv256:56
	R135:(uninterp) skey:71
	R136:(uninterp) skey:71
	R137:bv256:56
	R138:bv256:72
	R139:bv256:72
	R141:bv256:62
	R142:bv256:62
	R143:bv256:62
	R144:(uninterp) skey:71
	R145:bv256:71
	R146:(uninterp) skey:43
	R147:(uninterp) skey:43
	R148:bv256:71
	R149:bv256:43
	R151:(uninterp) skey:73
	R152:bv256:73
	R153:(uninterp) skey:74
	R154:(uninterp) skey:74
	R155:bv256:73
	R156:bv256:74
	R158:bv256:62
	R159:bv256:62
	R160:bv256:72
	R162:bv256:62
	R163:bv256:75
	R164:bv256:76
	R165:bv256:77
	R174:bv256:31
	R175:(uninterp) skey:56
	R176:bv256:31
	R177:bv256:56
	R178:bv256:68
	R181:bv256:31
	R182:(uninterp) skey:71
	R183:bv256:31
	R184:bv256:71
	R185:bv256:56
	R188:bv256:31
	R189:(uninterp) skey:73
	R190:bv256:31
	R191:bv256:73
	R192:bv256:62
	R194:bv256:62
	R195:bv256:62
	R196:bv256:68
	R197:bv256:68
	R199:bv256:31
	R200:(uninterp) skey:71
	R201:bv256:31
	R202:(uninterp) skey:71
	R203:bv256:68
	R204:bv256:68
	R207:bv256:31
	R208:(uninterp) skey:71
	R209:bv256:31
	R210:bv256:56
	R211:bv256:62
	R212:bv256:62
	R214:bv256:62
	R215:bv256:62
	R216:bv256:78
	R220:bv256:75
	R229:bv256:31
	R230:(uninterp) skey:78
	R231:bv256:31
	R232:bv256:78
	R233:bv256:79
	R236:bv256:31
	R237:(uninterp) skey:77
	R238:bv256:31
	R239:bv256:77
	R240:bv256:78
	R243:bv256:31
	R244:(uninterp) skey:56
	R245:bv256:31
	R246:bv256:56
	R247:bv256:68
	R249:(uninterp) skey:78
	R250:bv256:78
	R251:(uninterp) skey:77
	R252:bv256:77
	R253:bv256:77
	R256:(uninterp) skey:77
	R257:bv256:77
	R258:(uninterp) skey:65
	R259:bv256:65
	R260:bv256:65
	R263:(uninterp) skey:56
	R264:bv256:56
	R265:(uninterp) skey:71
	R266:bv256:71
	R267:bv256:71
	W115:wordmap:29
	lastHasThrown!!100:bool:80
	lastHasThrown!!131:bool:80
	lastHasThrown!!169:bool:80
	lastHasThrown!!171:bool:80
	lastHasThrown!!276:bool:80
	lastHasThrown!!278:bool:80
	lastHasThrown!!280:bool:80
	lastHasThrown!!282:bool:80
	CANON6!!107:wordmap:23
	tacAddress@1:bv256:10
	lastReverted!!101:bool:13
	lastReverted!!132:bool:13
	lastReverted!!170:bool:13
	lastReverted!!172:bool:13
	lastReverted!!277:bool:13
	lastReverted!!279:bool:13
	lastReverted!!281:bool:13
	lastReverted!!283:bool:13
	CANON13!!10:wordmap:36
	CANON14!!11:bv256:81
	LCANON0@1:bv256:55
	LCANON1@1:bool:42
	LCANON2@1:bv256:55
	LCANON3@1:bv256:56
	LCANON4@1:bool:43
	LCANON5@1:bool:43
	LCANON6@1:bool:44
	LCANON7@1:bv256:56
	LCANON8@1:bv256:56
	LCANON9@1:bv256:68
	CANON15!!12:bv256:82
	CANON16!!13:bv256:8
	CANON22!!124:wordmap:83
	CANON17!!14:bv256:30
	CANON10:wordmap:15
	CANON11:wordmap:2
	CANON12:wordmap:16
	CANON13:wordmap:36
	CANON14:bv256:81
	CANON15:bv256:82
	CANON16:bv256:8
	CANON17:bv256:30
	CANON18:bv256:40
	CANON19:bv256:84
	CANON20:wordmap:28
	CANON21:wordmap:35
	CANON22:wordmap:83
	CANON23:bv256:31
	CANON24:bool:31
	CANON25:bool:31
	CANON26:int:85
	CANON27:int:86
	CANON28:int:87
	CANON29:int:88
	CANON30:int:89
	CANON31:int:90
	CANON32:int:91
	CANON33:int:92
	CANON34:int:93
	CANON35:int:94
	CANON36:bool:95
	CANON37:int:96
	CANON38:int
	CANON39:int
	CANON40:int
	CANON41:int
	CANON42:int
	CANON43:wordmap:57
	CANON44:wordmap:57
	CANON45:wordmap:57
	CANON46:wordmap:58
	CANON47:wordmap:59
	CANON48:wordmap:59
	CANON49:wordmap:57
	CANON50:wordmap:59
	CANON51:wordmap:60
	CANON52:wordmap:60
	CANON53:wordmap:57
	CANON54:wordmap:57
	CANON55:wordmap:57
	CANON56:wordmap:58
	CANON57:bv256:49
	CANON58:bv256:50
	CANON59:bv256:51
	CANON60:bv256:52
	CANON61:bv256:53
	CANON62:bv256:54
	CANON63:wordmap:57
	CANON64:wordmap:57
	CANON65:wordmap:61
	CANON66:wordmap
	CANON67:wordmap
	CANON68:wordmap
	CANON69:wordmap
	CANON72:bv256:31
	CANON73:bv256
	CANON74:bv256
	CANON76:bv256:31
	CANON77:bool
	CANON78:bool
	CANON79:bool
	CANON81:ghostmap(bv256*bv256*bv256->bv256):26
	CANON82:bv256:31
	CANON84:bv256:31
	CANON95:bv256:31
	CANON97:bv256:31
	CANON98:bv256:31
	CANON99:bv256:31
	CANON14!!116:bv256:81
	CANON18!!15:bv256:40
	CANON19!!16:bv256:84
	LCANON10@1:bv256:56
	LCANON11@1:bv256:56
	LCANON12@1:bv256:71
	LCANON13@1:bv256:97
	LCANON14@1:bv256:71
	LCANON15@1:bool:43
	LCANON16@1:bool:44
	LCANON17@1:bool:70
	LCANON18@1:bool:62
	LCANON19@1:bv256:73
	LCANON20@1:bv256:73
	LCANON21@1:bv256:62
	LCANON22@1:bv256:73
	LCANON23@1:bv256:73
	LCANON24@1:bv256:74
	LCANON25@1:bv256:98
	LCANON26@1:bv256:73
	LCANON27@1:bv256:74
	LCANON28@1:bv256:75
	LCANON29@1:bv256:76
	LCANON30@1:bv256:77
	LCANON31@1:bool:63
	LCANON32@1:bool:63
	LCANON33@1:bool:64
	LCANON34@1:bv256:77
	LCANON35@1:bv256:77
	LCANON36@1:bv256:78
	LCANON37@1:bv256:77
	LCANON38@1:bv256:77
	LCANON39@1:bv256:65
	LCANON40@1:bv256:99
	LCANON41@1:bv256:65
	LCANON42@1:bool:63
	LCANON43@1:bool:64
	LCANON44@1:bool:69
	LCANON45@1:bool:56
	LCANON46@1:bv256:71
	LCANON47@1:bv256:71
	LCANON48@1:bv256:56
	LCANON49@1:bv256:71
	LCANON50@1:bv256:71
	LCANON51@1:bv256:43
	LCANON52@1:bv256:100
	LCANON53@1:bv256:71
	LCANON54@1:bv256:43
	LCANON55@1:bv256:62
	LCANON56@1:bv256:101
	LCANON57@1:bv256:72
	LCANON58@1:bool:62
	LCANON59@1:bv256:62
	LCANON60@1:bv256:102
	LCANON61@1:bv256:68
	LCANON62@1:bv256:71
	LCANON63@1:bv256:71
	LCANON64@1:bv256:68
	LCANON65@1:bv256:68
	LCANON66@1:bv256:71
	LCANON67@1:bv256:56
	LCANON68@1:bv256:62
	LCANON69@1:bv256:62
	LCANON70@1:bv256:62
	LCANON71@1:bv256:78
	LCANON72@1:bool:65
	LCANON73@1:bool:65
	LCANON74@1:bool:66
	LCANON75@1:bv256:78
	LCANON76@1:bv256:78
	LCANON77@1:bv256:79
	LCANON78@1:bv256:78
	LCANON79@1:bv256:78
	LCANON80@1:bv256:77
	LCANON81@1:bv256:103
	LCANON82@1:bv256:77
	LCANON83@1:bool:65
	LCANON84@1:bool:66
	LCANON85@1:bool:67
	LCANON86@1:bool:68
	LCANON87@1:bv256:56
	LCANON88@1:bv256:56
	LCANON89@1:bv256:68
	LCANON90@1:bv256:56
	LCANON91@1:bv256:56
	LCANON92@1:bv256:71
	LCANON93@1:bv256:104
	LCANON94@1:bv256:56
	LCANON95@1:bv256:72
	LCANON96@1:bv256:72
	LCANON97@1:bool:62
	LCANON98@1:bv256:62
	LCANON99@1:bv256:62
	tacContractAtCANON1:bv256:45
	tacContractAtCANON2:bv256:46
	tacContractAtCANON3:bv256:47
	tacContractsCreated!!126:wordmap:9
	CANON19!!121:bv256:84
	lastHasThrown:bool:80
	CANON2!!102:wordmap:17
	tacM0x20!!206:bv256:0
	tacContractsCreated:wordmap:9
	CANON7!!108:wordmap:24
	CANON1:int:105
	CANON2:wordmap:17
	CANON3:wordmap:20
	CANON4:wordmap:11
	CANON5:wordmap:22
	CANON6:wordmap:23
	CANON7:wordmap:24
	CANON8:wordmap:25
	CANON9:wordmap:12
	tacContractAtCANON:bv256:48
	CANON20!!17:wordmap:28
	CANON21!!18:wordmap:35
	CANON22!!19:wordmap:83
	CANON10!!111:wordmap:15
	tacSCANON0:wordmap:21
	tacCalldatasize!!3:bv256:27
	LCANON100@1:bv256:75
	CANON15!!117:bv256:82
	tacBalance!!127:wordmap:33
	lastStorageCANON10:wordmap:14
	lastStorageCANON11:wordmap:14
	lastStorageCANON12:wordmap:14
	lastStorageCANON13:wordmap:37
	lastStorageCANON14:bv256:106
	lastStorageCANON15:bv256:107
	lastStorageCANON16:bv256:108
	lastStorageCANON17:bv256:109
	lastStorageCANON18:bv256:110
	lastStorageCANON19:bv256:111
	lastStorageCANON20:wordmap:14
	lastStorageCANON21:wordmap:14
	lastStorageCANON22:wordmap:112
	lastStorageCANON23:wordmap:113
	lastStorageCANON24:wordmap:113
	lastStorageCANON25:wordmap:113
	lastStorageCANON26:wordmap:113
	lastHasThrown!!78:bool:80
	CANON3!!103:wordmap:20
	tacSighash!!35:bv256:114
	tacSighash@1:bv256:114
	CANON8!!109:wordmap:25
	CANON:int:115
}
Program {
	Block 0_0_0_0_0_0 Succ [1_0_0_1_0_0] {
		AssignHavocCmd tacM0x40!!0:1
		AssignHavocCmd R1:3
		AssumeExpCmd Ge(R1:3 0x1 )
		AssignHavocCmd tacCalldatasize!!3:27
		AssignHavocCmd tacExtcodesize!!5:19
		AssignHavocCmd tacBalance!!6:33
		AssignHavocCmd CANON10!!7:15
		AssignHavocCmd CANON11!!8:2
		AssignHavocCmd CANON12!!9:16
		AssignHavocCmd CANON13!!10:36
		AssignHavocCmd CANON14!!11:81
		AssignHavocCmd CANON15!!12:82
		AssignHavocCmd CANON16!!13:8
		AssignHavocCmd CANON17!!14:30
		AssignHavocCmd CANON18!!15:40
		AssignHavocCmd CANON19!!16:84
		AssignHavocCmd CANON20!!17:28
		AssignHavocCmd CANON21!!18:35
		AssignHavocCmd CANON22!!19:83
		AssignHavocCmd CANON26:85
		AssumeExpCmd LAnd(Ge(CANON26:85 0x0(int) ) Le(CANON26:85 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON27:86
		AssumeExpCmd LAnd(Ge(CANON27:86 0x0(int) ) Le(CANON27:86 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON28:87
		AssumeExpCmd LAnd(Ge(CANON28:87 0x0(int) ) Le(CANON28:87 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON29:88
		AssumeExpCmd LAnd(Ge(CANON29:88 0x0(int) ) Le(CANON29:88 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON30:89
		AssumeExpCmd LAnd(Ge(CANON30:89 0x0(int) ) Le(CANON30:89 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON31:90
		AssumeExpCmd LAnd(Ge(CANON31:90 0x0(int) ) Le(CANON31:90 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON32:91
		AssumeExpCmd LAnd(Ge(CANON32:91 0x0(int) ) Le(CANON32:91 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON33:92
		AssumeExpCmd LAnd(Ge(CANON33:92 0x0(int) ) Le(CANON33:92 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON34:93
		AssumeExpCmd LAnd(Ge(CANON34:93 0x0(int) ) Le(CANON34:93 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON35:94
		AssumeExpCmd LAnd(Ge(CANON35:94 0x0(int) ) Le(CANON35:94 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON81!20:26
		AssignHavocCmd R21:45
		AssumeExpCmd Eq(R21:45 0x1 )
		AssignHavocCmd R22:46
		AssumeExpCmd Eq(R22:46 0x2 )
		AssignHavocCmd R23:47
		AssumeExpCmd Eq(R23:47 0x4 )
		AssignHavocCmd CANON2!!25:17
		AssignHavocCmd CANON3!!26:20
		AssignHavocCmd CANON4!!27:11
		AssignHavocCmd CANON5!!28:22
		AssignHavocCmd CANON6!!29:23
		AssignHavocCmd CANON7!!30:24
		AssignHavocCmd CANON8!!31:25
		AssignHavocCmd CANON9!!32:12
		AssignHavocCmd R33:48
		AssumeExpCmd LAnd(Ge(R33:48 0x1 ) Le(R33:48 0xffffffffffffffffffffffffffffffffffffffff ) )
		AssignHavocCmd tacSCANON0!!34:21
		AssignHavocCmd tacSighash!!35:114
		AnnotationCmd JSON{"key":{"name":"tac.state.extension","type":"analysis.icfg.Inliner$ExtendedStateVars","erasureStrategy":"Canonical"},"value":"rO0ABXNyACdhbmFseXNpcy5pY2ZnLklubGluZXIkRXh0ZW5kZWRTdGF0ZVZhcnOvh/MjxNFkQAIAAUwAFmluc3RhbmNlVG9FeHRlbmRlZFZhcnN0AA9MamF2YS91dGlsL01hcDt4cHNyACFkYXRhc3RydWN0dXJlcy5MaW5rZWRBcnJheUhhc2hNYXAAAAAAAAAAAQMAAkYACmxvYWRGYWN0b3JMAAloYXNoVGFibGV0AC5MZGF0YXN0cnVjdHVyZXMvYXJyYXloYXNodGFibGUvQXJyYXlIYXNoVGFibGU7eHB3CAAAAAFAAAAAc3IAFGphdmEubWF0aC5CaWdJbnRlZ2VyjPyfH6k7+x0DAAZJAAhiaXRDb3VudEkACWJpdExlbmd0aEkAE2ZpcnN0Tm9uemVyb0J5dGVOdW1JAAxsb3dlc3RTZXRCaXRJAAZzaWdudW1bAAltYWduaXR1ZGV0AAJbQnhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cP///////////////v////4AAAABdXIAAltCrPMX+AYIVOACAAB4cAAAABDORgSgAAAAAAAAAAAAAAAXeHNxAH4AA3cIAAAAAEAAAAB4eA=="}
		AnnotationCmd:116 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssignHavocCmd CANON:115
		AssumeExpCmd LAnd(Ge(CANON:115 0x0(int) ) Le(CANON:115 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":0,"index":0,"sym":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":117,"charByteOffset":29},"end":{"line":117,"charByteOffset":44}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"tokenId"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"tokenId","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":117,"charByteOffset":29},"end":{"line":117,"charByteOffset":44}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":117,"charByteOffset":29},"end":{"line":117,"charByteOffset":44}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"tokenId"}]}},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Parameter","sourceName":"tokenId"},"fields":null}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":0}
		AnnotationCmd:117 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd:118 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":2}
		AnnotationCmd:119 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AssignExpCmd CANON1:105 R33:120
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":3}
		AnnotationCmd:121 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":4}
		AnnotationCmd:122 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":5}
		AnnotationCmd:123 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming contracts in scene with non-empty bytecode have EXTCODESIZE larger than zero"}}
		AssignExpCmd R36:31 Select(tacExtcodesize!!5:19 Apply(to_skey:bif R33:120) )
		AssumeExpCmd Ge(R36:31 0x1 )
		AssumeExpCmd Eq(R36:124 R1:125 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":6}
		AnnotationCmd:126 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming address(0).code has no code deployed"}}
		AssignExpCmd B38:31 Eq(Select(tacExtcodesize!!5:19 Apply(skey_basic:bif 0x0) ) 0x0 )
		AssumeCmd B38:31
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":7}
		AnnotationCmd:127 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":8}
		AnnotationCmd:128 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":9}
		AnnotationCmd:129 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish addresses of precompiled contracts"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":10}
		AnnotationCmd:130 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":11}
		AnnotationCmd:131 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"static links"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":12}
		AnnotationCmd:132 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":13}
		AnnotationCmd:133 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":14}
		AnnotationCmd:134 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":15}
		AnnotationCmd:135 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Constrain immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":16}
		AnnotationCmd:136 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish equivalence of extension and base contract immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":17}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1}
		AnnotationCmd:137 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Declaration","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}},"cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"id":"e","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.CVLVar","id":"e18802"},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Variable"},"fields":[[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"coinbase"}],{"namePrefix":"CANON31","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.coinbase"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"basefee"}],{"namePrefix":"CANON29","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.basefee"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"timestamp"}],{"namePrefix":"CANON35","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.timestamp"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"blobbasefee"}],{"namePrefix":"CANON30","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.blobbasefee"}]},[{"#class":"tac.DataField.StructField","field":"tx"},{"#class":"tac.DataField.StructField","field":"origin"}],{"namePrefix":"CANON28","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.tx.origin"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"sender"}],{"namePrefix":"CANON26","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.sender"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"value"}],{"namePrefix":"CANON27","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.value"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"difficulty"}],{"namePrefix":"CANON32","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.difficulty"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"gaslimit"}],{"namePrefix":"CANON33","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.gaslimit"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"number"}],{"namePrefix":"CANON34","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":118,"charByteOffset":4},"end":{"line":118,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.number"}]}]}}
		AnnotationCmd:138 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":18}
		AnnotationCmd:139 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":119,"charByteOffset":4},"end":{"line":119,"charByteOffset":66}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":119,"charByteOffset":4},"end":{"line":119,"charByteOffset":20}},"id":"zeroAddr","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":119,"charByteOffset":4},"end":{"line":119,"charByteOffset":20}}}}],"exp":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":119,"charByteOffset":23},"end":{"line":119,"charByteOffset":65}}},"printHint":"16"},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:140 CANON36:95 false
		AnnotationCmd:141 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":19}
		AnnotationCmd:142 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":120,"charByteOffset":4},"end":{"line":120,"charByteOffset":24}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":120,"charByteOffset":4},"end":{"line":120,"charByteOffset":17}},"id":"value","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":120,"charByteOffset":4},"end":{"line":120,"charByteOffset":17}}}}],"exp":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"64","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"64"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":120,"charByteOffset":20},"end":{"line":120,"charByteOffset":23}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:143 CANON37:96 0x64
		AnnotationCmd:144 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":20}
		AnnotationCmd:145 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":122,"charByteOffset":4},"end":{"line":122,"charByteOffset":52}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"to_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"value_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"sighashInt":{"n":"8cb0a511"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":122,"charByteOffset":23},"end":{"line":122,"charByteOffset":24}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"tokenId","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":122,"charByteOffset":26},"end":{"line":122,"charByteOffset":33}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"zeroAddr","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":122,"charByteOffset":35},"end":{"line":122,"charByteOffset":43}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"value","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":122,"charByteOffset":45},"end":{"line":122,"charByteOffset":50}}},"twoStateIndex":"NEITHER"}],"noRevert":false,"storage":{"id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"range":{"#class":"utils.Range.Empty","comment":"empty storage type"}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":122,"charByteOffset":4},"end":{"line":122,"charByteOffset":51}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"to_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"value_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"sighashInt":{"n":"8cb0a511"}},"definitelyNonPayable":false,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false,"virtual":false},"stateMutability":"payable","evmExternalMethodInfo":{"sigHash":"8cb0a511","name":"approve","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"resultTypes":[],"stateMutability":"payable","isConstant":false,"paramNames":["tokenId_","to_","value_"],"isLibrary":false,"contractName":"ERC3525","contractInstanceId":"ce4604a0000000000000000000000017","sourceSegment":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":147,"charByteOffset":4},"end":{"line":154,"charByteOffset":5}},"content":"function approve(uint256 tokenId_, address to_, uint256 value_) public payable virtual override {\n        address owner = ERC3525.ownerOf(tokenId_);\n        require(to_ != owner, \"ERC3525: approval to current owner\");\n\n        require(_isApprovedOrOwner(_msgSender(), tokenId_), \"ERC3525: approve caller is not owner nor approved\");\n\n        _approveValue(tokenId_, to_, value_);\n    }"}}},"hasEnv":true}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"certoraArg1880518806"},"src":{"id":"e18802"}}}
		AssignExpCmd:146 I41 CANON:115
		AssignExpCmd:147 I42 0x0(int)
		AssignExpCmd:148 I43 0x64(int)
	}
	Block 1_0_0_1_0_0 Succ [2_0_0_1_0_0, 3_0_0_1_0_0] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"CANON70","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0}}}
		AssertCmd:149 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:150 R71:31 Apply(safe_math_narrow_bv256:bif CANON26:85)
		AssignExpCmd:150 R73 Select(tacBalance!!6:33 Apply(to_skey:bif R71:31) )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.ReadBalanceSnippet","balance":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R73","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R71","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		AssertCmd:151 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd B75 Le(Apply(safe_math_narrow_bv256:bif CANON27:86) R73 )
		JumpiCmd:150 2_0_0_1_0_0 3_0_0_1_0_0 B75
	}
	Block 2_0_0_1_0_0 Succ [15108_1012_0_1_0_1, 15272_1010_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"summary":null,"convention":{"#class":"analysis.icfg.Inliner.CallConventionType.FromCVL"},"calleeId":1,"isNoRevert":false}}
		AssignHavocCmd:150 tacCalldatasize!!76:27
		AssumeExpCmd Eq(tacCalldatasize!!76:27 0x64 )
		AssignExpCmd:150 tacCalldatabuf@1:41 MapDefinition(CANON80.30722:bv256 -> Ite(Lt(CANON80.30722 tacCalldatasize!!76:27 ) Select(Select(Select(CANON81!20:26 CANON80.30722 ) tacCalldatasize!!76:27 ) 0x8cb0a511 ) 0x0 ) bytemap)
		AssignExpCmd:150 R77:31 Select(Select(Select(CANON81!20:26 0x0 ) 0x64 ) 0x8cb0a511 )
		AssumeExpCmd LAnd(Ge(R77:31 0x8cb0a51100000000000000000000000000000000000000000000000000000000 ) Le(R77:31 0x8cb0a511ffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd:150 JSON{"key":{"name":"cvl.arg-serialization.start","type":"spec.CVLInvocationCompiler$StartSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":1}}
		LabelCmd:150 "202: Read primitive from certoraArg1880718808:int..."
		AssertCmd:152 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:152 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:150 tacCalldatabufCANON0@1:153 Apply(safe_math_narrow_bv256:bif I41)
		LabelCmd:150 "...done 202"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I41","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"0","callId":1,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"fields":null}}
		LabelCmd:150 "203: Read primitive from certoraArg1880918810:int..."
		AssertCmd:154 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:154 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:150 tacCalldatabufCANON1@1:6 false
		LabelCmd:150 "...done 203"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I42","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"20","callId":1,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"fields":null}}
		LabelCmd:150 "204: Read primitive from certoraArg1881118812:int..."
		AssertCmd:155 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:155 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:150 tacCalldatabufCANON2@1:7 0x64
		LabelCmd:150 "...done 204"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I43","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"40","callId":1,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"fields":null}}
		AnnotationCmd:150 JSON{"key":{"name":"cvl.arg-serialization.end","type":"spec.CVLInvocationCompiler$EndSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":1}}
		AssignExpCmd:150 lastHasThrown!!78:80 false
		AssertCmd:156 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:150 R79:31 Apply(safe_math_narrow_bv256:bif CANON26:85)
		AssertCmd:157 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:158 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:159 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:160 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:161 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:162 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:163 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:164 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:165 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:166 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:150 R81:31 Apply(safe_math_narrow_bv256:bif CANON27:86)
		AssertCmd:167 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:150 R82:31 Apply(safe_math_narrow_bv256:bif CANON26:85)
		AssignExpCmd:150 R85:31 Select(tacBalance!!6:33 Apply(to_skey:bif R82:31) )
		AssignExpCmd:168 I86:31 IntSub(R85:31 R81:31 )
		AssignExpCmd:168 tacBalance!!87:33 Store(tacBalance!!6:33 Apply(to_skey:bif R82:31) I86:31 )
		AssignExpCmd:150 R88:31 Select(tacBalance!!87:33 Apply(to_skey:bif R33:120) )
		AssignExpCmd:168 I89:31 IntAdd(R88:31 R81:31)
		AssumeExpCmd LAnd(Ge(I89:31 0x0(int) ) Le(I89:31 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssumeExpCmd Apply(add_noofl_256:bif R88:31 R81:31)
		AssignExpCmd:168 R91:31 Apply(safe_math_narrow_bv256:bif I89:31)
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.TransferSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R85","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I86","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R82","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R88","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R91","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R33","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"tacContractAt"}},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC3525"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R81","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:150 "Start procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd:150 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:150 R92:31 Select(tacExtcodesize!!5:19 Apply(to_skey:bif R33:169) )
		AssumeExpCmd Ge(R92:31 0x1 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R33","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacAddress","maybeTACKeywordOrdinal":22}},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC3525"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]},"contractInstance":"ce4604a0000000000000000000000017","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R92","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"storageType":null,"range":null}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":{"unresolvedFunctions":[]}}
		AnnotationCmd:150 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":0,"bytecodeCount":8,"sources":[{"source":7,"begin":589,"end":48232}]}}
		LabelCmd "→ Assuming FP is strictly monotonic increasing"
		AssumeExpCmd Le(tacM0x40!!0:1 0x80 )
		LabelCmd "←"
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":13,"bytecodeCount":9,"sources":[{"source":7,"begin":589,"end":48232}]}}
		AssumeExpCmd Eq(tacSighash!!35:114 0x8cb0a511 )
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":29,"bytecodeCount":5,"sources":[{"source":7,"begin":589,"end":48232}]}}
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":137,"bytecodeCount":6,"sources":[{"source":7,"begin":589,"end":48232}]}}
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":149,"bytecodeCount":5,"sources":[{"source":7,"begin":589,"end":48232}]}}
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":160,"bytecodeCount":5,"sources":[{"source":7,"begin":589,"end":48232}]}}
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":171,"bytecodeCount":5,"sources":[{"source":7,"begin":589,"end":48232}]}}
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":182,"bytecodeCount":5,"sources":[{"source":7,"begin":589,"end":48232}]}}
		AnnotationCmd:170 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":1196,"bytecodeCount":14,"sources":[{"source":7,"begin":9047,"end":9896}]}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23021,"bytecodeCount":12,"sources":[{"source":16,"begin":4783,"end":5402},{"source":16,"begin":4860,"end":4866},{"source":16,"begin":4868,"end":4874},{"source":16,"begin":4876,"end":4882},{"source":16,"begin":4925,"end":4927},{"source":16,"begin":4913,"end":4922},{"source":16,"begin":4904,"end":4911},{"source":16,"begin":4900,"end":4923},{"source":16,"begin":4896,"end":4928},{"source":16,"begin":4893,"end":5012}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":0,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":147,"charByteOffset":4},"end":{"line":154,"charByteOffset":5}},"content":"compiler-generate condition in function approve(uint256 tokenId_, address to_, uint256 value_) public payable virtual override "}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":0}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23044,"bytecodeCount":9,"sources":[{"source":16,"begin":4893,"end":5012},{"source":16,"begin":5051,"end":5052},{"source":16,"begin":5076,"end":5129},{"source":16,"begin":5121,"end":5128},{"source":16,"begin":5112,"end":5118},{"source":16,"begin":5101,"end":5110},{"source":16,"begin":5097,"end":5119}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22766,"bytecodeCount":10,"sources":[{"source":16,"begin":2964,"end":3103},{"source":16,"begin":3010,"end":3015},{"source":16,"begin":3048,"end":3054},{"source":16,"begin":3035,"end":3055},{"source":16,"begin":3026,"end":3055},{"source":16,"begin":3064,"end":3097},{"source":16,"begin":3091,"end":3096}]}}
		AssignExpCmd:172 R93:55 tacCalldatabufCANON0@1:173
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22744,"bytecodeCount":5,"sources":[{"source":16,"begin":2836,"end":2958},{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2927,"end":2932}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22735,"bytecodeCount":9,"sources":[{"source":16,"begin":2753,"end":2830},{"source":16,"begin":2790,"end":2797},{"source":16,"begin":2819,"end":2824},{"source":16,"begin":2808,"end":2824}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22753,"bytecodeCount":5,"sources":[{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2902,"end":2907},{"source":16,"begin":2899,"end":2934},{"source":16,"begin":2889,"end":2952}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22763,"bytecodeCount":3,"sources":[{"source":16,"begin":2889,"end":2952},{"source":16,"begin":2836,"end":2958}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22780,"bytecodeCount":6,"sources":[{"source":16,"begin":3064,"end":3097},{"source":16,"begin":2964,"end":3103}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23057,"bytecodeCount":12,"sources":[{"source":16,"begin":5076,"end":5129},{"source":16,"begin":5066,"end":5129},{"source":16,"begin":5022,"end":5139},{"source":16,"begin":5178,"end":5180},{"source":16,"begin":5204,"end":5257},{"source":16,"begin":5249,"end":5256},{"source":16,"begin":5240,"end":5246},{"source":16,"begin":5229,"end":5238},{"source":16,"begin":5225,"end":5247}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22939,"bytecodeCount":10,"sources":[{"source":16,"begin":4158,"end":4297},{"source":16,"begin":4204,"end":4209},{"source":16,"begin":4242,"end":4248},{"source":16,"begin":4229,"end":4249},{"source":16,"begin":4220,"end":4249},{"source":16,"begin":4258,"end":4291},{"source":16,"begin":4285,"end":4290}]}}
		AssignExpCmd:174 B94:42 false
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22917,"bytecodeCount":5,"sources":[{"source":16,"begin":4030,"end":4152},{"source":16,"begin":4103,"end":4127},{"source":16,"begin":4121,"end":4126}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22860,"bytecodeCount":6,"sources":[{"source":16,"begin":3576,"end":3672},{"source":16,"begin":3613,"end":3620},{"source":16,"begin":3642,"end":3666},{"source":16,"begin":3660,"end":3665}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22829,"bytecodeCount":11,"sources":[{"source":16,"begin":3444,"end":3570},{"source":16,"begin":3481,"end":3488},{"source":16,"begin":3521,"end":3563},{"source":16,"begin":3514,"end":3519},{"source":16,"begin":3510,"end":3564},{"source":16,"begin":3499,"end":3564}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22870,"bytecodeCount":7,"sources":[{"source":16,"begin":3642,"end":3666},{"source":16,"begin":3631,"end":3666},{"source":16,"begin":3576,"end":3672}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22926,"bytecodeCount":5,"sources":[{"source":16,"begin":4103,"end":4127},{"source":16,"begin":4096,"end":4101},{"source":16,"begin":4093,"end":4128},{"source":16,"begin":4083,"end":4146}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22936,"bytecodeCount":3,"sources":[{"source":16,"begin":4083,"end":4146},{"source":16,"begin":4030,"end":4152}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22953,"bytecodeCount":6,"sources":[{"source":16,"begin":4258,"end":4291},{"source":16,"begin":4158,"end":4297}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23074,"bytecodeCount":12,"sources":[{"source":16,"begin":5204,"end":5257},{"source":16,"begin":5194,"end":5257},{"source":16,"begin":5149,"end":5267},{"source":16,"begin":5306,"end":5308},{"source":16,"begin":5332,"end":5385},{"source":16,"begin":5377,"end":5384},{"source":16,"begin":5368,"end":5374},{"source":16,"begin":5357,"end":5366},{"source":16,"begin":5353,"end":5375}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22766,"bytecodeCount":10,"sources":[{"source":16,"begin":2964,"end":3103},{"source":16,"begin":3010,"end":3015},{"source":16,"begin":3048,"end":3054},{"source":16,"begin":3035,"end":3055},{"source":16,"begin":3026,"end":3055},{"source":16,"begin":3064,"end":3097},{"source":16,"begin":3091,"end":3096}]}}
		AssignExpCmd:172 R95:55 0x64
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22744,"bytecodeCount":5,"sources":[{"source":16,"begin":2836,"end":2958},{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2927,"end":2932}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22735,"bytecodeCount":9,"sources":[{"source":16,"begin":2753,"end":2830},{"source":16,"begin":2790,"end":2797},{"source":16,"begin":2819,"end":2824},{"source":16,"begin":2808,"end":2824}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22753,"bytecodeCount":5,"sources":[{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2902,"end":2907},{"source":16,"begin":2899,"end":2934},{"source":16,"begin":2889,"end":2952}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22763,"bytecodeCount":3,"sources":[{"source":16,"begin":2889,"end":2952},{"source":16,"begin":2836,"end":2958}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22780,"bytecodeCount":6,"sources":[{"source":16,"begin":3064,"end":3097},{"source":16,"begin":2964,"end":3103}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23091,"bytecodeCount":10,"sources":[{"source":16,"begin":5332,"end":5385},{"source":16,"begin":5322,"end":5385},{"source":16,"begin":5277,"end":5395},{"source":16,"begin":4783,"end":5402}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":1217,"bytecodeCount":3,"sources":[{"source":7,"begin":9047,"end":9896}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":6536,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}},{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"B94","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.was.replaced.with.bool","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":2,"logicalPosition":1,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}},{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R95","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":3,"logicalPosition":2,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"to_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"value_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":7,"begin":9047,"len":849,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6536,"bytecodeCount":18,"sources":[{"source":7,"begin":9047,"end":9896},{"source":7,"begin":9246,"end":9259},{"source":7,"begin":9178,"end":9244},{"source":7,"begin":9171,"end":9260},{"source":7,"begin":9336,"end":9337},{"source":7,"begin":9268,"end":9334},{"source":7,"begin":9261,"end":9338},{"source":7,"begin":9414,"end":9416},{"source":7,"begin":9346,"end":9412},{"source":7,"begin":9339,"end":9417},{"source":7,"begin":9493,"end":9499},{"source":7,"begin":9425,"end":9491},{"source":7,"begin":9418,"end":9500},{"source":7,"begin":9511,"end":9524},{"source":7,"begin":9527,"end":9552},{"source":7,"begin":9543,"end":9551},{"source":7,"begin":9527,"end":9542}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":5774,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"ownerOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":9527,"len":25,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:175 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":5774,"bytecodeCount":18,"sources":[{"source":7,"begin":4670,"end":5396},{"source":7,"begin":4743,"end":4757},{"source":7,"begin":4862,"end":4875},{"source":7,"begin":4794,"end":4860},{"source":7,"begin":4787,"end":4876},{"source":7,"begin":4952,"end":4953},{"source":7,"begin":4884,"end":4950},{"source":7,"begin":4877,"end":4954},{"source":7,"begin":5030,"end":5031},{"source":7,"begin":4962,"end":5028},{"source":7,"begin":4955,"end":5032},{"source":7,"begin":5108,"end":5116},{"source":7,"begin":5040,"end":5106},{"source":7,"begin":5033,"end":5117},{"source":7,"begin":5128,"end":5152},{"source":7,"begin":5143,"end":5151},{"source":7,"begin":5128,"end":5142}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":9356,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":5128,"len":24,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:176 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9356,"bytecodeCount":17,"sources":[{"source":7,"begin":21590,"end":22085},{"source":7,"begin":21757,"end":21770},{"source":7,"begin":21689,"end":21755},{"source":7,"begin":21682,"end":21771},{"source":7,"begin":21847,"end":21848},{"source":7,"begin":21779,"end":21845},{"source":7,"begin":21772,"end":21849},{"source":7,"begin":21925,"end":21926},{"source":7,"begin":21857,"end":21923},{"source":7,"begin":21850,"end":21927},{"source":7,"begin":22003,"end":22011},{"source":7,"begin":21935,"end":22001},{"source":7,"begin":21928,"end":22012},{"source":7,"begin":22031,"end":22048},{"source":7,"begin":22039,"end":22047},{"source":7,"begin":22031,"end":22038}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":15108,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":22031,"len":17,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:177 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15108,"bytecodeCount":26,"sources":[{"source":7,"begin":21051,"end":21584},{"source":7,"begin":21117,"end":21121},{"source":7,"begin":21226,"end":21239},{"source":7,"begin":21158,"end":21224},{"source":7,"begin":21151,"end":21240},{"source":7,"begin":21316,"end":21317},{"source":7,"begin":21248,"end":21314},{"source":7,"begin":21241,"end":21318},{"source":7,"begin":21394,"end":21395},{"source":7,"begin":21326,"end":21392},{"source":7,"begin":21319,"end":21396},{"source":7,"begin":21472,"end":21480},{"source":7,"begin":21404,"end":21470},{"source":7,"begin":21397,"end":21481},{"source":7,"begin":21520,"end":21521},{"source":7,"begin":21499,"end":21509},{"source":7,"begin":21499,"end":21516},{"source":7,"begin":21499,"end":21521},{"source":7,"begin":21499,"end":21577}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":32}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B97:43 Eq(CANON17!!14:178 0x0 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":1,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":93}},"content":"_allTokens.length != 0 && _allTokens[_allTokensIndex[tokenId_]].id == tokenId_"}}}
		JumpiCmd:179 15108_1012_0_1_0_1 15272_1010_0_1_0_0 B97:43
	}
	Block 3_0_0_1_0_0 Succ [4_0_0_0_0_0] {
		AssignExpCmd:150 lastHasThrown!!100:80 false
		AssignExpCmd:150 lastReverted!!101:13 true
		AnnotationCmd:150 JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		JumpCmd:150 4_0_0_0_0_0
	}
	Block 4_0_0_0_0_0 Succ [] {
		AssignExpCmd:180 CANON2!!102:17 CANON2!!25:17
		AssignExpCmd:180 CANON3!!103:20 CANON3!!26:20
		AssignExpCmd:180 CANON4!!104:11 CANON4!!27:11
		AssignExpCmd:180 tacSCANON0!!105:21 tacSCANON0!!34:21
		AssignExpCmd:180 CANON5!!106:22 CANON5!!28:22
		AssignExpCmd:180 CANON6!!107:23 CANON6!!29:23
		AssignExpCmd:180 CANON7!!108:24 CANON7!!30:24
		AssignExpCmd:180 CANON8!!109:25 CANON8!!31:25
		AssignExpCmd:180 CANON9!!110:12 CANON9!!32:12
		AssignExpCmd:180 CANON10!!111:15 CANON10!!7:15
		AssignExpCmd:180 CANON11!!112:2 CANON11!!8:2
		AssignExpCmd:180 CANON12!!113:16 CANON12!!9:16
		AssignExpCmd:180 CANON13!!114:36 CANON13!!10:36
		AssignExpCmd:180 CANON14!!116:81 CANON14!!11:81
		AssignExpCmd:180 CANON15!!117:82 CANON15!!12:82
		AssignExpCmd:180 CANON16!!118:8 CANON16!!13:8
		AssignExpCmd:180 CANON17!!119:30 CANON17!!14:30
		AssignExpCmd:180 CANON18!!120:40 CANON18!!15:40
		AssignExpCmd:180 CANON19!!121:84 CANON19!!16:84
		AssignExpCmd:180 CANON20!!122:28 CANON20!!17:28
		AssignExpCmd:180 CANON21!!123:35 CANON21!!18:35
		AssignExpCmd:180 CANON22!!124:83 CANON22!!19:83
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageRestoreSnapshot","name":{"namePrefix":"CANON70","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:150 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":21}
		AnnotationCmd:181 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":124,"charByteOffset":4},"end":{"line":124,"charByteOffset":67}},"type":null,"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":124,"charByteOffset":4},"end":{"line":124,"charByteOffset":67}},"id":"_","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Bottom"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":124,"charByteOffset":4},"end":{"line":124,"charByteOffset":67}}}}],"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastReverted","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":124,"charByteOffset":11},"end":{"line":124,"charByteOffset":23}}},"twoStateIndex":"NEITHER"},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:182 B129 true
		AnnotationCmd:183 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":22}
		AnnotationCmd:184 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":117,"charByteOffset":0},"end":{"line":125,"charByteOffset":1}},"exp":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Empty"}}},"description":"sanity check for rule approveZeroAddressFails succeeded","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:185 B130 false
		AssertCmd:186 false "sanity check for rule approveZeroAddressFails succeeded"
	}
	Block 5_0_0_1_0_2 Succ [4_0_0_0_0_0] {
		AssignExpCmd:150 lastHasThrown!!131:80 false
		AssignExpCmd:150 lastReverted!!132:13 true
		AnnotationCmd:150 JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Revert","range":null}}
		LabelCmd:150 "End procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd:150 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
	}
	Block 2835_1008_0_1_0_0 Succ [12941_1013_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":17}}
		AnnotationCmd:187 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":2835,"bytecodeCount":29,"sources":[{"source":7,"begin":15913,"end":15950},{"source":7,"begin":15913,"end":15959},{"source":7,"begin":15906,"end":15959},{"source":7,"begin":15417,"end":15966}]}}
		AssignExpCmd:187 R133:56 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:187 R134:56 Mul(0x6 R177:56 )
		AssignExpCmd:187 R135:71 Apply(skey_add:bif R133:56 R134:56)
		AssignExpCmd:188 R136:71 Apply(skey_add:bif R135:71 0x4)
		AssignExpCmd:189 R137:56 AnnotationExp(Select(CANON8!!31:25 R136:190 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R177","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"80"}}]}})
		AssumeExpCmd Le(R137:56 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R137","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"approved","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R177","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":228,"charByteOffset":15},"end":{"line":228,"charByteOffset":61}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":10,"rets":[{"s":{"namePrefix":"R137","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"getApproved"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:191 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12917,"bytecodeCount":4,"sources":[{"source":7,"begin":20062,"end":20091},{"source":7,"begin":20062,"end":20104}]}}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12917_1012_0_0_0_0 -> 12941_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R767:bv256 := R1236:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12917_1012_0_0_0_0 -> 12941_1013_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2835_1008_0_0_0_0 -> 12941_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R336:bv256 := R334:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2835_1008_0_0_0_0 -> 12941_1013_0_0_0_0"}
		LabelCmd "Parallel assignment for R143:bv256 := R141:bv256"
		AssignExpCmd R143:62 Ite(Eq(R137:72 R79:192 ) 0x1 0x0 )
	}
	Block 5968_1009_0_1_0_0 Succ [4_0_0_1_0_3825, 6162_1011_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":10}}
		AnnotationCmd:193 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":5968,"bytecodeCount":37,"sources":[{"source":7,"begin":5171,"end":5208},{"source":7,"begin":5171,"end":5214},{"source":7,"begin":5162,"end":5214},{"source":7,"begin":5314,"end":5320},{"source":7,"begin":5247,"end":5313},{"source":7,"begin":5240,"end":5321},{"source":7,"begin":5357,"end":5358},{"source":7,"begin":5339,"end":5359},{"source":7,"begin":5339,"end":5345},{"source":7,"begin":5331,"end":5389}]}}
		AssignExpCmd:193 R144:71 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:193 R145:71 Mul(0x6 R184:71 )
		AssignExpCmd:193 R146:43 Apply(skey_add:bif R144:71 R145:71)
		AssignExpCmd:194 R147:43 Apply(skey_add:bif R146:43 0x3)
		AssignExpCmd:195 R148:71 AnnotationExp(Select(CANON6!!29:23 R147:196 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R184","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"60"}}]}})
		AssumeExpCmd Le(R148:71 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R148","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"owner","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R184","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":17},"end":{"line":100,"charByteOffset":60}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.SourceFinderSnippet.LocalAssignmentSnippet","lhs":"owner_","finderType":0,"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":8},"end":{"line":100,"charByteOffset":60}},"value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R148","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1010}]}}}
		AssignExpCmd:150 B150:31 Eq(R148:71 0x0 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":11,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":101,"charByteOffset":8},"end":{"line":101,"charByteOffset":66}},"content":"require(owner_ != address(0), \\\"ERC3525: invalid token ID\\\")"}}}
		JumpiCmd:197 4_0_0_1_0_3825 6162_1011_0_1_0_0 B150:31
	}
	Block 5968_1014_0_1_0_0 Succ [4_0_0_1_0_3825, 6162_1016_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":4}}
		AnnotationCmd:193 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":5968,"bytecodeCount":37,"sources":[{"source":7,"begin":5171,"end":5208},{"source":7,"begin":5171,"end":5214},{"source":7,"begin":5162,"end":5214},{"source":7,"begin":5314,"end":5320},{"source":7,"begin":5247,"end":5313},{"source":7,"begin":5240,"end":5321},{"source":7,"begin":5357,"end":5358},{"source":7,"begin":5339,"end":5359},{"source":7,"begin":5339,"end":5345},{"source":7,"begin":5331,"end":5389}]}}
		AssignExpCmd:193 R151:73 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:193 R152:73 Mul(0x6 R191:73 )
		AssignExpCmd:193 R153:74 Apply(skey_add:bif R151:73 R152:73)
		AssignExpCmd:194 R154:74 Apply(skey_add:bif R153:74 0x3)
		AssignExpCmd:195 R155:73 AnnotationExp(Select(CANON6!!29:23 R154:198 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R191","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"60"}}]}})
		AssumeExpCmd Le(R155:73 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R155","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"owner","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R191","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":17},"end":{"line":100,"charByteOffset":60}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.SourceFinderSnippet.LocalAssignmentSnippet","lhs":"owner_","finderType":0,"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":8},"end":{"line":100,"charByteOffset":60}},"value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R155","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]}}}
		AssignExpCmd:150 B157:31 Eq(R155:73 0x0 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":5,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":101,"charByteOffset":8},"end":{"line":101,"charByteOffset":66}},"content":"require(owner_ != address(0), \\\"ERC3525: invalid token ID\\\")"}}}
		JumpiCmd:197 4_0_0_1_0_3825 6162_1016_0_1_0_0 B157:31
	}
	Block 6162_1011_0_1_0_0 Succ [12778_1013_0_1_0_4, 12868_1013_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":11}}
		AnnotationCmd:197 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6162,"bytecodeCount":5,"sources":[{"source":7,"begin":5331,"end":5389},{"source":7,"begin":4670,"end":5396}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"R148","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"ownerOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:199 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12778,"bytecodeCount":16,"sources":[{"source":7,"begin":19808,"end":19833},{"source":7,"begin":19792,"end":19833},{"source":7,"begin":19933,"end":19938},{"source":7,"begin":19866,"end":19932},{"source":7,"begin":19859,"end":19939},{"source":7,"begin":19983,"end":19988},{"source":7,"begin":19970,"end":19988},{"source":7,"begin":19970,"end":19979},{"source":7,"begin":19970,"end":20046}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.SourceFinderSnippet.LocalAssignmentSnippet","lhs":"owner","finderType":0,"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":266,"charByteOffset":8},"end":{"line":266,"charByteOffset":49}},"value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R148","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]}}}
		AssignExpCmd:150 B161:62 Eq(R79:200 R148:101 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":12,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":268,"charByteOffset":12},"end":{"line":269,"charByteOffset":54}},"content":"operator_ == owner ||\nERC3525.isApprovedForAll(owner, operator_)"}}}
		JumpiCmd:201 12778_1013_0_1_0_4 12868_1013_0_1_0_0 B161:62
	}
	Block 6162_1016_0_1_0_0 Succ [15108_1007_0_1_0_3, 15272_1005_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":5}}
		AnnotationCmd:197 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6162,"bytecodeCount":5,"sources":[{"source":7,"begin":5331,"end":5389},{"source":7,"begin":4670,"end":5396}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R155","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"ownerOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:199 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6693,"bytecodeCount":15,"sources":[{"source":7,"begin":9527,"end":9552},{"source":7,"begin":9511,"end":9552},{"source":7,"begin":9652,"end":9657},{"source":7,"begin":9585,"end":9651},{"source":7,"begin":9578,"end":9658},{"source":7,"begin":9683,"end":9688},{"source":7,"begin":9676,"end":9688},{"source":7,"begin":9676,"end":9679},{"source":7,"begin":9668,"end":9727}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.SourceFinderSnippet.LocalAssignmentSnippet","lhs":"owner","finderType":0,"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":148,"charByteOffset":8},"end":{"line":148,"charByteOffset":49}},"value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R155","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":6,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":149,"charByteOffset":8},"end":{"line":149,"charByteOffset":67}},"content":"require(to_ != owner, \\\"ERC3525: approval to current owner\\\")"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":6}}
		AnnotationCmd:202 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6840,"bytecodeCount":5,"sources":[{"source":7,"begin":9668,"end":9727},{"source":7,"begin":9746,"end":9788},{"source":7,"begin":9765,"end":9777},{"source":7,"begin":9765,"end":9775}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":9578,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"Context"},"methodId":"_msgSender"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":9765,"len":12,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:203 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9578,"bytecodeCount":16,"sources":[{"source":0,"begin":656,"end":1026},{"source":0,"begin":709,"end":716},{"source":0,"begin":821,"end":834},{"source":0,"begin":753,"end":819},{"source":0,"begin":746,"end":835},{"source":0,"begin":911,"end":912},{"source":0,"begin":843,"end":909},{"source":0,"begin":836,"end":913},{"source":0,"begin":989,"end":990},{"source":0,"begin":921,"end":987},{"source":0,"begin":914,"end":991},{"source":0,"begin":1009,"end":1019},{"source":0,"begin":1002,"end":1019}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[{"s":{"namePrefix":"R79","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"Context"},"methodId":"_msgSender"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:204 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6851,"bytecodeCount":4,"sources":[{"source":7,"begin":9765,"end":9777},{"source":7,"begin":9779,"end":9787},{"source":7,"begin":9746,"end":9764},{"source":7,"begin":9746,"end":9788}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":12620,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R79","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}},{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":2,"logicalPosition":1,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_isApprovedOrOwner"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"operator_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":7,"begin":9746,"len":42,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:205 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12620,"bytecodeCount":19,"sources":[{"source":7,"begin":19321,"end":20121},{"source":7,"begin":19417,"end":19421},{"source":7,"begin":19526,"end":19539},{"source":7,"begin":19458,"end":19524},{"source":7,"begin":19451,"end":19540},{"source":7,"begin":19616,"end":19617},{"source":7,"begin":19548,"end":19614},{"source":7,"begin":19541,"end":19618},{"source":7,"begin":19694,"end":19695},{"source":7,"begin":19626,"end":19692},{"source":7,"begin":19619,"end":19696},{"source":7,"begin":19772,"end":19780},{"source":7,"begin":19704,"end":19770},{"source":7,"begin":19697,"end":19781},{"source":7,"begin":19792,"end":19805},{"source":7,"begin":19808,"end":19833},{"source":7,"begin":19824,"end":19832},{"source":7,"begin":19808,"end":19823}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":5774,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"ownerOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":19808,"len":25,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:206 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":5774,"bytecodeCount":18,"sources":[{"source":7,"begin":4670,"end":5396},{"source":7,"begin":4743,"end":4757},{"source":7,"begin":4862,"end":4875},{"source":7,"begin":4794,"end":4860},{"source":7,"begin":4787,"end":4876},{"source":7,"begin":4952,"end":4953},{"source":7,"begin":4884,"end":4950},{"source":7,"begin":4877,"end":4954},{"source":7,"begin":5030,"end":5031},{"source":7,"begin":4962,"end":5028},{"source":7,"begin":4955,"end":5032},{"source":7,"begin":5108,"end":5116},{"source":7,"begin":5040,"end":5106},{"source":7,"begin":5033,"end":5117},{"source":7,"begin":5128,"end":5152},{"source":7,"begin":5143,"end":5151},{"source":7,"begin":5128,"end":5142}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":7,"startPc":9356,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":5128,"len":24,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:176 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9356,"bytecodeCount":17,"sources":[{"source":7,"begin":21590,"end":22085},{"source":7,"begin":21757,"end":21770},{"source":7,"begin":21689,"end":21755},{"source":7,"begin":21682,"end":21771},{"source":7,"begin":21847,"end":21848},{"source":7,"begin":21779,"end":21845},{"source":7,"begin":21772,"end":21849},{"source":7,"begin":21925,"end":21926},{"source":7,"begin":21857,"end":21923},{"source":7,"begin":21850,"end":21927},{"source":7,"begin":22003,"end":22011},{"source":7,"begin":21935,"end":22001},{"source":7,"begin":21928,"end":22012},{"source":7,"begin":22031,"end":22048},{"source":7,"begin":22039,"end":22047},{"source":7,"begin":22031,"end":22038}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":8,"startPc":15108,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":22031,"len":17,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:177 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15108,"bytecodeCount":26,"sources":[{"source":7,"begin":21051,"end":21584},{"source":7,"begin":21117,"end":21121},{"source":7,"begin":21226,"end":21239},{"source":7,"begin":21158,"end":21224},{"source":7,"begin":21151,"end":21240},{"source":7,"begin":21316,"end":21317},{"source":7,"begin":21248,"end":21314},{"source":7,"begin":21241,"end":21318},{"source":7,"begin":21394,"end":21395},{"source":7,"begin":21326,"end":21392},{"source":7,"begin":21319,"end":21396},{"source":7,"begin":21472,"end":21480},{"source":7,"begin":21404,"end":21470},{"source":7,"begin":21397,"end":21481},{"source":7,"begin":21520,"end":21521},{"source":7,"begin":21499,"end":21509},{"source":7,"begin":21499,"end":21516},{"source":7,"begin":21499,"end":21521},{"source":7,"begin":21499,"end":21577}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1003}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":32}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B166:63 Eq(CANON17!!14:207 0x0 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":7,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":93}},"content":"_allTokens.length != 0 && _allTokens[_allTokensIndex[tokenId_]].id == tokenId_"}}}
		JumpiCmd:179 15108_1007_0_1_0_3 15272_1005_0_1_0_0 B166:63
	}
	Block 6862_1019_0_1_0_0 Succ [4_0_0_0_0_0] {
		AnnotationCmd:208 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6862,"bytecodeCount":11,"sources":[{"source":7,"begin":9738,"end":9842}]}}
		AnnotationCmd:150 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25781,"bytecodeCount":18,"sources":[{"source":16,"begin":25510,"end":25929},{"source":16,"begin":25676,"end":25680},{"source":16,"begin":25714,"end":25716},{"source":16,"begin":25703,"end":25712},{"source":16,"begin":25699,"end":25717},{"source":16,"begin":25691,"end":25717},{"source":16,"begin":25763,"end":25772},{"source":16,"begin":25757,"end":25761},{"source":16,"begin":25753,"end":25773},{"source":16,"begin":25749,"end":25750},{"source":16,"begin":25738,"end":25747},{"source":16,"begin":25734,"end":25751},{"source":16,"begin":25727,"end":25774},{"source":16,"begin":25791,"end":25922},{"source":16,"begin":25917,"end":25921}]}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25747,"bytecodeCount":7,"sources":[{"source":16,"begin":25138,"end":25504},{"source":16,"begin":25280,"end":25283},{"source":16,"begin":25301,"end":25368},{"source":16,"begin":25365,"end":25367},{"source":16,"begin":25360,"end":25363}]}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22601,"bytecodeCount":15,"sources":[{"source":16,"begin":1623,"end":1792},{"source":16,"begin":1707,"end":1718},{"source":16,"begin":1741,"end":1747},{"source":16,"begin":1736,"end":1739},{"source":16,"begin":1729,"end":1748},{"source":16,"begin":1781,"end":1785},{"source":16,"begin":1776,"end":1779},{"source":16,"begin":1772,"end":1786},{"source":16,"begin":1757,"end":1786}]}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25759,"bytecodeCount":7,"sources":[{"source":16,"begin":25301,"end":25368},{"source":16,"begin":25294,"end":25368},{"source":16,"begin":25377,"end":25470},{"source":16,"begin":25466,"end":25469}]}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25669,"bytecodeCount":13,"sources":[{"source":16,"begin":24896,"end":25132},{"source":16,"begin":25036,"end":25070},{"source":16,"begin":25032,"end":25033},{"source":16,"begin":25024,"end":25030},{"source":16,"begin":25020,"end":25034},{"source":16,"begin":25013,"end":25071},{"source":16,"begin":25105,"end":25124},{"source":16,"begin":25100,"end":25102},{"source":16,"begin":25092,"end":25098},{"source":16,"begin":25088,"end":25103},{"source":16,"begin":25081,"end":25125}]}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25770,"bytecodeCount":10,"sources":[{"source":16,"begin":25377,"end":25470},{"source":16,"begin":25495,"end":25497},{"source":16,"begin":25490,"end":25493},{"source":16,"begin":25486,"end":25498},{"source":16,"begin":25479,"end":25498},{"source":16,"begin":25138,"end":25504}]}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25804,"bytecodeCount":7,"sources":[{"source":16,"begin":25791,"end":25922},{"source":16,"begin":25783,"end":25922},{"source":16,"begin":25510,"end":25929}]}}
		AnnotationCmd:209 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6911,"bytecodeCount":8,"sources":[{"source":7,"begin":9738,"end":9842}]}}
		AssignExpCmd:208 lastHasThrown!!169:80 false
		AssignExpCmd:208 lastReverted!!170:13 true
		AnnotationCmd:208 JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Revert","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":151,"charByteOffset":8},"end":{"line":151,"charByteOffset":112}}}}
		LabelCmd:150 "End procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd:150 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
	}
	Block 6920_1019_0_1_0_0 Succ [4_0_0_0_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":18}}
		AnnotationCmd:208 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6920,"bytecodeCount":7,"sources":[{"source":7,"begin":9738,"end":9842},{"source":7,"begin":9853,"end":9889},{"source":7,"begin":9867,"end":9875},{"source":7,"begin":9877,"end":9880},{"source":7,"begin":9882,"end":9888},{"source":7,"begin":9853,"end":9866}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":13,"startPc":13584,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}},{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"B94","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.was.replaced.with.bool","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":2,"logicalPosition":1,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}},{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R95","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":3,"logicalPosition":2,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_approveValue"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"to_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"value_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":7,"begin":9853,"len":36,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:210 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":13584,"bytecodeCount":22,"sources":[{"source":7,"begin":34636,"end":35437},{"source":7,"begin":34856,"end":34869},{"source":7,"begin":34788,"end":34854},{"source":7,"begin":34781,"end":34870},{"source":7,"begin":34946,"end":34947},{"source":7,"begin":34878,"end":34944},{"source":7,"begin":34871,"end":34948},{"source":7,"begin":35024,"end":35026},{"source":7,"begin":34956,"end":35022},{"source":7,"begin":34949,"end":35027},{"source":7,"begin":35103,"end":35109},{"source":7,"begin":35035,"end":35101},{"source":7,"begin":35028,"end":35110},{"source":7,"begin":35144,"end":35145},{"source":7,"begin":35129,"end":35146},{"source":7,"begin":35129,"end":35132},{"source":7,"begin":35121,"end":35193}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":19,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":432,"charByteOffset":8},"end":{"line":432,"charByteOffset":80}},"content":"require(to_ != address(0), \\\"ERC3525: approve value to the zero address\\\")"}}}
		AnnotationCmd:211 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":13783,"bytecodeCount":11,"sources":[{"source":7,"begin":35121,"end":35193}]}}
		AnnotationCmd:150 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":27756,"bytecodeCount":18,"sources":[{"source":16,"begin":40254,"end":40673},{"source":16,"begin":40420,"end":40424},{"source":16,"begin":40458,"end":40460},{"source":16,"begin":40447,"end":40456},{"source":16,"begin":40443,"end":40461},{"source":16,"begin":40435,"end":40461},{"source":16,"begin":40507,"end":40516},{"source":16,"begin":40501,"end":40505},{"source":16,"begin":40497,"end":40517},{"source":16,"begin":40493,"end":40494},{"source":16,"begin":40482,"end":40491},{"source":16,"begin":40478,"end":40495},{"source":16,"begin":40471,"end":40518},{"source":16,"begin":40535,"end":40666},{"source":16,"begin":40661,"end":40665}]}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":27722,"bytecodeCount":7,"sources":[{"source":16,"begin":39882,"end":40248},{"source":16,"begin":40024,"end":40027},{"source":16,"begin":40045,"end":40112},{"source":16,"begin":40109,"end":40111},{"source":16,"begin":40104,"end":40107}]}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22601,"bytecodeCount":15,"sources":[{"source":16,"begin":1623,"end":1792},{"source":16,"begin":1707,"end":1718},{"source":16,"begin":1741,"end":1747},{"source":16,"begin":1736,"end":1739},{"source":16,"begin":1729,"end":1748},{"source":16,"begin":1781,"end":1785},{"source":16,"begin":1776,"end":1779},{"source":16,"begin":1772,"end":1786},{"source":16,"begin":1757,"end":1786}]}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":27734,"bytecodeCount":7,"sources":[{"source":16,"begin":40045,"end":40112},{"source":16,"begin":40038,"end":40112},{"source":16,"begin":40121,"end":40214},{"source":16,"begin":40210,"end":40213}]}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":27644,"bytecodeCount":13,"sources":[{"source":16,"begin":39647,"end":39876},{"source":16,"begin":39787,"end":39821},{"source":16,"begin":39783,"end":39784},{"source":16,"begin":39775,"end":39781},{"source":16,"begin":39771,"end":39785},{"source":16,"begin":39764,"end":39822},{"source":16,"begin":39856,"end":39868},{"source":16,"begin":39851,"end":39853},{"source":16,"begin":39843,"end":39849},{"source":16,"begin":39839,"end":39854},{"source":16,"begin":39832,"end":39869}]}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":27745,"bytecodeCount":10,"sources":[{"source":16,"begin":40121,"end":40214},{"source":16,"begin":40239,"end":40241},{"source":16,"begin":40234,"end":40237},{"source":16,"begin":40230,"end":40242},{"source":16,"begin":40223,"end":40242},{"source":16,"begin":39882,"end":40248}]}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":27779,"bytecodeCount":7,"sources":[{"source":16,"begin":40535,"end":40666},{"source":16,"begin":40527,"end":40666},{"source":16,"begin":40254,"end":40673}]}}
		AnnotationCmd:212 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":13832,"bytecodeCount":8,"sources":[{"source":7,"begin":35121,"end":35193}]}}
		AssignExpCmd:211 lastHasThrown!!171:80 false
		AssignExpCmd:211 lastReverted!!172:13 true
		AnnotationCmd:211 JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Revert","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":432,"charByteOffset":8},"end":{"line":432,"charByteOffset":80}}}}
		LabelCmd:150 "End procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd:150 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
	}
	Block 9575_1008_0_1_0_0 Succ [5_0_0_1_0_2, 2835_1008_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":16}}
		AnnotationCmd:213 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9575,"bytecodeCount":3,"sources":[{"source":7,"begin":22023,"end":22078},{"source":7,"begin":21590,"end":22085}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":11,"rets":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]}}}
		AnnotationCmd:214 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":2798,"bytecodeCount":23,"sources":[{"source":7,"begin":15872,"end":15896},{"source":7,"begin":15913,"end":15923},{"source":7,"begin":15924,"end":15939},{"source":7,"begin":15924,"end":15949},{"source":7,"begin":15940,"end":15948},{"source":7,"begin":15913,"end":15950}]}}
		AssignExpCmd:150 R174:31 0x6
		AssignExpCmd:215 R175:56 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:216) Apply(skey_basic:bif 0x6))
		AssignExpCmd:217 R177:56 AnnotationExp(Select(CANON3!!26:20 R175:218 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R175","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R177","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!76","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":228,"charByteOffset":26},"end":{"line":228,"charByteOffset":51}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":228,"charByteOffset":15},"end":{"line":228,"charByteOffset":52}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B179:31 Le(CANON17!!14:219 R177:56 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":17,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":228,"charByteOffset":15},"end":{"line":228,"charByteOffset":52}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		JumpiCmd:187 5_0_0_1_0_2 2835_1008_0_1_0_0 B179:31
	}
	Block 9575_1009_0_1_0_0 Succ [4_0_0_1_0_3824, 5968_1009_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":9}}
		AnnotationCmd:213 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9575,"bytecodeCount":3,"sources":[{"source":7,"begin":22023,"end":22078},{"source":7,"begin":21590,"end":22085}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":7,"rets":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]}}}
		AnnotationCmd:214 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":5931,"bytecodeCount":23,"sources":[{"source":7,"begin":5128,"end":5152},{"source":7,"begin":5171,"end":5181},{"source":7,"begin":5182,"end":5197},{"source":7,"begin":5182,"end":5207},{"source":7,"begin":5198,"end":5206},{"source":7,"begin":5171,"end":5208}]}}
		AssignExpCmd:150 R181:31 0x6
		AssignExpCmd:220 R182:71 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:216) Apply(skey_basic:bif 0x6))
		AssignExpCmd:221 R184:71 AnnotationExp(Select(CANON3!!26:20 R182:222 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R182","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R184","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!76","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":28},"end":{"line":100,"charByteOffset":53}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":17},"end":{"line":100,"charByteOffset":54}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B186:31 Le(CANON17!!14:178 R184:71 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":10,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":17},"end":{"line":100,"charByteOffset":54}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		JumpiCmd:193 4_0_0_1_0_3824 5968_1009_0_1_0_0 B186:31
	}
	Block 9575_1014_0_1_0_0 Succ [4_0_0_1_0_3824, 5968_1014_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":3}}
		AnnotationCmd:213 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9575,"bytecodeCount":3,"sources":[{"source":7,"begin":22023,"end":22078},{"source":7,"begin":21590,"end":22085}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]}}}
		AnnotationCmd:214 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":5931,"bytecodeCount":23,"sources":[{"source":7,"begin":5128,"end":5152},{"source":7,"begin":5171,"end":5181},{"source":7,"begin":5182,"end":5197},{"source":7,"begin":5182,"end":5207},{"source":7,"begin":5198,"end":5206},{"source":7,"begin":5171,"end":5208}]}}
		AssignExpCmd:150 R188:31 0x6
		AssignExpCmd:220 R189:73 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:216) Apply(skey_basic:bif 0x6))
		AssignExpCmd:221 R191:73 AnnotationExp(Select(CANON3!!26:20 R189:223 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R189","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R191","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!76","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":28},"end":{"line":100,"charByteOffset":53}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":17},"end":{"line":100,"charByteOffset":54}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B193:31 Le(CANON17!!14:224 R191:73 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":4,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":17},"end":{"line":100,"charByteOffset":54}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		JumpiCmd:193 4_0_0_1_0_3824 5968_1014_0_1_0_0 B193:31
	}
	Block 12778_1013_0_1_0_4 Succ [12879_1013_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12778_1013_0_0_0_0 -> 12879_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R746:bv256 := R721:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12778_1013_0_0_0_0 -> 12879_1013_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12778_1013_0_0_0_99 -> 12879_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R221:bv256 := R196:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12778_1013_0_0_0_99 -> 12879_1013_0_0_0_0"}
		LabelCmd "Parallel assignment for R195:bv256 := R162:bv256"
		AssignExpCmd R195:62 0x1
	}
	Block 12868_1013_0_1_0_0 Succ [12879_1013_0_1_0_0] {
		AnnotationCmd:201 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12868,"bytecodeCount":6,"sources":[{"source":7,"begin":19970,"end":20046},{"source":7,"begin":20004,"end":20046},{"source":7,"begin":20029,"end":20034},{"source":7,"begin":20036,"end":20045},{"source":7,"begin":20004,"end":20028}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":9,"startPc":9064,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R148","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}},{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R79","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":2,"logicalPosition":1,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"isApprovedForAll"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"operator_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":7,"begin":20004,"len":42,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:225 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9064,"bytecodeCount":68,"sources":[{"source":7,"begin":16495,"end":17025},{"source":7,"begin":16594,"end":16598},{"source":7,"begin":16703,"end":16716},{"source":7,"begin":16635,"end":16701},{"source":7,"begin":16628,"end":16717},{"source":7,"begin":16793,"end":16794},{"source":7,"begin":16725,"end":16791},{"source":7,"begin":16718,"end":16795},{"source":7,"begin":16871,"end":16872},{"source":7,"begin":16803,"end":16869},{"source":7,"begin":16796,"end":16873},{"source":7,"begin":16949,"end":16958},{"source":7,"begin":16881,"end":16947},{"source":7,"begin":16874,"end":16959},{"source":7,"begin":16977,"end":16989},{"source":7,"begin":16977,"end":16997},{"source":7,"begin":16990,"end":16996},{"source":7,"begin":16977,"end":17007},{"source":7,"begin":16977,"end":17018},{"source":7,"begin":17008,"end":17017},{"source":7,"begin":16970,"end":17018}]}}
		AssignExpCmd:150 R199:31 0x7
		AssignExpCmd:226 R200:71 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R148:227) Apply(skey_basic:bif 0x7))
		AssignExpCmd:228 R202:71 Apply(skey_add:bif R200:71 0x2)
		AssignExpCmd:229 R208:71 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R79:230) R202:231)
		AssignExpCmd:232 R210:56 AnnotationExp(Select(CANON22!!19:83 R208:233 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"7"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R148","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"7"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R200","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"2"}},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R79","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R202","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R208","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"0"}}]}})
		AssumeExpCmd Le(R210:56 0xff )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R210","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R79","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"approvals","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R148","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_addressData"}}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":236,"charByteOffset":15},"end":{"line":236,"charByteOffset":56}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":9,"rets":[{"s":{"namePrefix":"R210","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"isApprovedForAll"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"operator_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:234 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12878,"bytecodeCount":1,"sources":[{"source":7,"begin":20004,"end":20046}]}}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12878_1013_0_0_0_0 -> 12879_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R746:bv256 := R798:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12878_1013_0_0_0_0 -> 12879_1013_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12868_1013_0_0_0_0 -> 12879_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R221:bv256 := R219:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12868_1013_0_0_0_0 -> 12879_1013_0_0_0_0"}
		LabelCmd "Parallel assignment for R195:bv256 := R210:bv256"
		AssignExpCmd R195:62 R210:62
	}
	Block 12879_1013_0_1_0_0 Succ [12879_1013_0_1_0_5, 12885_1013_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":12}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12879,"bytecodeCount":4,"sources":[{"source":7,"begin":19970,"end":20046},{"source":7,"begin":19970,"end":20104}]}}
		AssignExpCmd B213:31 Le(R195:62 0x0 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":13,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":268,"charByteOffset":12},"end":{"line":270,"charByteOffset":54}},"content":"operator_ == owner ||\nERC3525.isApprovedForAll(owner, operator_) ||"}}}
		JumpiCmd:235 12885_1013_0_1_0_0 12879_1013_0_1_0_5 B213:31
	}
	Block 12879_1013_0_1_0_5 Succ [12941_1013_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12879_1013_0_0_0_0 -> 12941_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R767:bv256 := R746:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12879_1013_0_0_0_0 -> 12941_1013_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12879_1013_0_0_0_101 -> 12941_1013_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R336:bv256 := R221:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"12879_1013_0_0_0_101 -> 12941_1013_0_0_0_0"}
		LabelCmd "Parallel assignment for R143:bv256 := R195:bv256"
		AssignExpCmd R143:62 R195:101
	}
	Block 12885_1013_0_1_0_0 Succ [15108_1006_0_1_0_6, 15272_1004_0_1_0_0] {
		AnnotationCmd:235 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12885,"bytecodeCount":8,"sources":[{"source":7,"begin":19970,"end":20104},{"source":7,"begin":20095,"end":20104},{"source":7,"begin":20062,"end":20104},{"source":7,"begin":20062,"end":20091},{"source":7,"begin":20082,"end":20090},{"source":7,"begin":20062,"end":20081}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":10,"startPc":2641,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"getApproved"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":20062,"len":29,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:236 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":2641,"bytecodeCount":18,"sources":[{"source":7,"begin":15417,"end":15966},{"source":7,"begin":15494,"end":15501},{"source":7,"begin":15606,"end":15619},{"source":7,"begin":15538,"end":15604},{"source":7,"begin":15531,"end":15620},{"source":7,"begin":15696,"end":15697},{"source":7,"begin":15628,"end":15694},{"source":7,"begin":15621,"end":15698},{"source":7,"begin":15774,"end":15775},{"source":7,"begin":15706,"end":15772},{"source":7,"begin":15699,"end":15776},{"source":7,"begin":15852,"end":15860},{"source":7,"begin":15784,"end":15850},{"source":7,"begin":15777,"end":15861},{"source":7,"begin":15872,"end":15896},{"source":7,"begin":15887,"end":15895},{"source":7,"begin":15872,"end":15886}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":11,"startPc":9356,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":15872,"len":24,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:237 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9356,"bytecodeCount":17,"sources":[{"source":7,"begin":21590,"end":22085},{"source":7,"begin":21757,"end":21770},{"source":7,"begin":21689,"end":21755},{"source":7,"begin":21682,"end":21771},{"source":7,"begin":21847,"end":21848},{"source":7,"begin":21779,"end":21845},{"source":7,"begin":21772,"end":21849},{"source":7,"begin":21925,"end":21926},{"source":7,"begin":21857,"end":21923},{"source":7,"begin":21850,"end":21927},{"source":7,"begin":22003,"end":22011},{"source":7,"begin":21935,"end":22001},{"source":7,"begin":21928,"end":22012},{"source":7,"begin":22031,"end":22048},{"source":7,"begin":22039,"end":22047},{"source":7,"begin":22031,"end":22038}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":12,"startPc":15108,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":22031,"len":17,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:177 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15108,"bytecodeCount":26,"sources":[{"source":7,"begin":21051,"end":21584},{"source":7,"begin":21117,"end":21121},{"source":7,"begin":21226,"end":21239},{"source":7,"begin":21158,"end":21224},{"source":7,"begin":21151,"end":21240},{"source":7,"begin":21316,"end":21317},{"source":7,"begin":21248,"end":21314},{"source":7,"begin":21241,"end":21318},{"source":7,"begin":21394,"end":21395},{"source":7,"begin":21326,"end":21392},{"source":7,"begin":21319,"end":21396},{"source":7,"begin":21472,"end":21480},{"source":7,"begin":21404,"end":21470},{"source":7,"begin":21397,"end":21481},{"source":7,"begin":21520,"end":21521},{"source":7,"begin":21499,"end":21509},{"source":7,"begin":21499,"end":21516},{"source":7,"begin":21499,"end":21521},{"source":7,"begin":21499,"end":21577}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1002}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":32}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B217:65 Eq(CANON17!!14:238 0x0 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":14,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":93}},"content":"_allTokens.length != 0 && _allTokens[_allTokensIndex[tokenId_]].id == tokenId_"}}}
		JumpiCmd:179 15108_1006_0_1_0_6 15272_1004_0_1_0_0 B217:65
	}
	Block 12941_1013_0_1_0_0 Succ [6862_1019_0_1_0_0, 6920_1019_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":13}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":12941,"bytecodeCount":9,"sources":[{"source":7,"begin":19970,"end":20104},{"source":7,"begin":19949,"end":20114},{"source":7,"begin":19321,"end":20121}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"R143","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_isApprovedOrOwner"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"operator_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:239 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6857,"bytecodeCount":3,"sources":[{"source":7,"begin":9746,"end":9788},{"source":7,"begin":9738,"end":9842}]}}
		AssignExpCmd B221:31 Le(R143:62 0x0 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":18,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":151,"charByteOffset":8},"end":{"line":151,"charByteOffset":112}},"content":"require(_isApprovedOrOwner(_msgSender(), tokenId_), \\\"ERC3525: approve caller is not owner nor approved\\\")"}}}
		JumpiCmd:208 6862_1019_0_1_0_0 6920_1019_0_1_0_0 B221:31
	}
	Block 15108_1006_0_1_0_6 Succ [15327_1004_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1006_0_0_0_0 -> 15327_1004_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R949:bv256 := R898:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1006_0_0_0_0 -> 15327_1004_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1006_0_0_0_102 -> 15327_1004_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R283:bv256 := R229:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1006_0_0_0_102 -> 15327_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for B223:bool := B218:bool"
		AssignExpCmd B223:66 false
	}
	Block 15108_1007_0_1_0_3 Succ [15327_1005_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1007_0_0_0_0 -> 15327_1005_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R573:bv256 := R528:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1007_0_0_0_0 -> 15327_1005_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1007_0_0_0_97 -> 15327_1005_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R160:bv256 := R128:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1007_0_0_0_97 -> 15327_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for B225:bool := B167:bool"
		AssignExpCmd B225:64 false
	}
	Block 15108_1012_0_1_0_1 Succ [15327_1010_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1012_0_0_0_0 -> 15327_1010_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R231:bv256 := R205:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1012_0_0_0_0 -> 15327_1010_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1012_0_0_0_95 -> 15327_1010_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R74:bv256 := R54:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15108_1012_0_0_0_95 -> 15327_1010_0_0_0_0"}
		LabelCmd "Parallel assignment for B227:bool := B98:bool"
		AssignExpCmd B227:44 false
	}
	Block 15272_1004_0_1_0_0 Succ [4_0_0_1_0_3827, 15310_1002_0_1_0_0] {
		AnnotationCmd:179 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15272,"bytecodeCount":24,"sources":[{"source":7,"begin":21499,"end":21577},{"source":7,"begin":21569,"end":21577},{"source":7,"begin":21525,"end":21535},{"source":7,"begin":21536,"end":21551},{"source":7,"begin":21536,"end":21561},{"source":7,"begin":21552,"end":21560},{"source":7,"begin":21525,"end":21562}]}}
		AssignExpCmd:150 R229:31 0x6
		AssignExpCmd:240 R230:78 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:216) Apply(skey_basic:bif 0x6))
		AssignExpCmd:241 R232:78 AnnotationExp(Select(CANON3!!26:20 R230:242 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R230","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1002}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R232","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1002}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!76","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":52},"end":{"line":283,"charByteOffset":77}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B234:31 Le(CANON17!!14:243 R232:78 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":15,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		JumpiCmd:244 4_0_0_1_0_3827 15310_1002_0_1_0_0 B234:31
	}
	Block 15272_1005_0_1_0_0 Succ [4_0_0_1_0_3827, 15310_1003_0_1_0_0] {
		AnnotationCmd:179 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15272,"bytecodeCount":24,"sources":[{"source":7,"begin":21499,"end":21577},{"source":7,"begin":21569,"end":21577},{"source":7,"begin":21525,"end":21535},{"source":7,"begin":21536,"end":21551},{"source":7,"begin":21536,"end":21561},{"source":7,"begin":21552,"end":21560},{"source":7,"begin":21525,"end":21562}]}}
		AssignExpCmd:150 R236:31 0x6
		AssignExpCmd:240 R237:77 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:216) Apply(skey_basic:bif 0x6))
		AssignExpCmd:241 R239:77 AnnotationExp(Select(CANON3!!26:20 R237:245 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R237","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1003}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R239","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1003}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!76","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":52},"end":{"line":283,"charByteOffset":77}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1002}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B241:31 Le(CANON17!!14:246 R239:77 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":8,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		JumpiCmd:244 4_0_0_1_0_3827 15310_1003_0_1_0_0 B241:31
	}
	Block 15272_1010_0_1_0_0 Succ [5_0_0_1_0_2, 15310_1008_0_1_0_0] {
		AnnotationCmd:179 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15272,"bytecodeCount":24,"sources":[{"source":7,"begin":21499,"end":21577},{"source":7,"begin":21569,"end":21577},{"source":7,"begin":21525,"end":21535},{"source":7,"begin":21536,"end":21551},{"source":7,"begin":21536,"end":21561},{"source":7,"begin":21552,"end":21560},{"source":7,"begin":21525,"end":21562}]}}
		AssignExpCmd:150 R243:31 0x6
		AssignExpCmd:240 R244:56 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:216) Apply(skey_basic:bif 0x6))
		AssignExpCmd:241 R246:56 AnnotationExp(Select(CANON3!!26:20 R244:247 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R244","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R246","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!76","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":52},"end":{"line":283,"charByteOffset":77}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:150 B248:31 Le(CANON17!!14:248 R246:56 )
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":2,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		JumpiCmd:244 5_0_0_1_0_2 15310_1008_0_1_0_0 B248:31
	}
	Block 15310_1002_0_1_0_0 Succ [15327_1004_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":15}}
		AnnotationCmd:244 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15310,"bytecodeCount":15,"sources":[{"source":7,"begin":21525,"end":21562},{"source":7,"begin":21525,"end":21565},{"source":7,"begin":21525,"end":21577}]}}
		AssignExpCmd:244 R249:78 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:244 R250:78 Mul(0x6 R232:78 )
		AssignExpCmd:244 R251:77 Apply(skey_add:bif R249:78 R250:78)
		AssignExpCmd:249 R253:77 AnnotationExp(Select(CANON11!!8:2 R251:250 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R232","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1002}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R253","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1003}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"id","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R232","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1002}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":81}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1002_0_0_0_0 -> 15327_1004_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R949:bv256 := R1017:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1002_0_0_0_0 -> 15327_1004_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1002_0_0_0_0 -> 15327_1004_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R283:bv256 := R281:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1002_0_0_0_0 -> 15327_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for B223:bool := B254:bool"
		AssignExpCmd B223:66 Eq(R253:77 tacCalldatabufCANON0@1:216 )
	}
	Block 15310_1003_0_1_0_0 Succ [15327_1005_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":8}}
		AnnotationCmd:244 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15310,"bytecodeCount":15,"sources":[{"source":7,"begin":21525,"end":21562},{"source":7,"begin":21525,"end":21565},{"source":7,"begin":21525,"end":21577}]}}
		AssignExpCmd:244 R256:77 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:244 R257:77 Mul(0x6 R239:77 )
		AssignExpCmd:244 R258:65 Apply(skey_add:bif R256:77 R257:77)
		AssignExpCmd:249 R260:65 AnnotationExp(Select(CANON11!!8:2 R258:251 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R239","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1003}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R260","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1004}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"id","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R239","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1003}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":81}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1003_0_0_0_0 -> 15327_1005_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R573:bv256 := R600:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1003_0_0_0_0 -> 15327_1005_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1003_0_0_0_0 -> 15327_1005_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R160:bv256 := R158:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1003_0_0_0_0 -> 15327_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for B225:bool := B261:bool"
		AssignExpCmd B225:64 Eq(R260:65 tacCalldatabufCANON0@1:216 )
	}
	Block 15310_1008_0_1_0_0 Succ [15327_1010_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":2}}
		AnnotationCmd:244 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15310,"bytecodeCount":15,"sources":[{"source":7,"begin":21525,"end":21562},{"source":7,"begin":21525,"end":21565},{"source":7,"begin":21525,"end":21577}]}}
		AssignExpCmd:244 R263:56 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:244 R264:56 Mul(0x6 R246:56 )
		AssignExpCmd:244 R265:71 Apply(skey_add:bif R263:56 R264:56)
		AssignExpCmd:249 R267:71 AnnotationExp(Select(CANON11!!8:2 R265:252 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R246","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R267","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"id","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R246","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":81}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1008_0_0_0_0 -> 15327_1010_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R231:bv256 := R251:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1008_0_0_0_0 -> 15327_1010_0_0_0_0"}
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1008_0_0_0_0 -> 15327_1010_0_0_0_0"}
		LabelCmd:150 "Parallel assignment for R74:bv256 := R72:bv256"
		AnnotationCmd:150 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1008_0_0_0_0 -> 15327_1010_0_0_0_0"}
		LabelCmd "Parallel assignment for B227:bool := B268:bool"
		AssignExpCmd B227:44 Eq(R267:71 tacCalldatabufCANON0@1:216 )
	}
	Block 15327_1004_0_1_0_0 Succ [4_0_0_1_0_3826, 9575_1008_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":14}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15327,"bytecodeCount":7,"sources":[{"source":7,"begin":21499,"end":21577},{"source":7,"begin":21492,"end":21577},{"source":7,"begin":21051,"end":21584}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":12,"rets":[{"s":{"namePrefix":"B223","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.was.replaced.with.bool","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:253 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9512,"bytecodeCount":3,"sources":[{"source":7,"begin":22031,"end":22048},{"source":7,"begin":22023,"end":22078}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":16,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":287,"charByteOffset":8},"end":{"line":287,"charByteOffset":63}},"content":"require(_exists(tokenId_), \\\"ERC3525: invalid token ID\\\")"}}}
		JumpiCmd:213 9575_1008_0_1_0_0 4_0_0_1_0_3826 B223:67
	}
	Block 15327_1005_0_1_0_0 Succ [4_0_0_1_0_3826, 9575_1009_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":7}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15327,"bytecodeCount":7,"sources":[{"source":7,"begin":21499,"end":21577},{"source":7,"begin":21492,"end":21577},{"source":7,"begin":21051,"end":21584}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":8,"rets":[{"s":{"namePrefix":"B225","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.was.replaced.with.bool","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:253 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9512,"bytecodeCount":3,"sources":[{"source":7,"begin":22031,"end":22048},{"source":7,"begin":22023,"end":22078}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":9,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":287,"charByteOffset":8},"end":{"line":287,"charByteOffset":63}},"content":"require(_exists(tokenId_), \\\"ERC3525: invalid token ID\\\")"}}}
		JumpiCmd:213 9575_1009_0_1_0_0 4_0_0_1_0_3826 B225:69
	}
	Block 15327_1010_0_1_0_0 Succ [4_0_0_1_0_3826, 9575_1014_0_1_0_0] {
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":1}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15327,"bytecodeCount":7,"sources":[{"source":7,"begin":21499,"end":21577},{"source":7,"begin":21492,"end":21577},{"source":7,"begin":21051,"end":21584}]}}
		AnnotationCmd:150 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"B227","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.was.replaced.with.bool","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:253 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9512,"bytecodeCount":3,"sources":[{"source":7,"begin":22031,"end":22048},{"source":7,"begin":22023,"end":22078}]}}
		AnnotationCmd:150 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":3,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":287,"charByteOffset":8},"end":{"line":287,"charByteOffset":63}},"content":"require(_exists(tokenId_), \\\"ERC3525: invalid token ID\\\")"}}}
		JumpiCmd:213 9575_1014_0_1_0_0 4_0_0_1_0_3826 B227:70
	}
	Block 4_0_0_1_0_3824 Succ [4_0_0_0_0_0] {
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":5960,"bytecodeCount":3,"sources":[{"source":7,"begin":5171,"end":5208}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":24261,"bytecodeCount":10,"sources":[{"source":16,"begin":14056,"end":14236},{"source":16,"begin":14104,"end":14181},{"source":16,"begin":14101,"end":14102},{"source":16,"begin":14094,"end":14182},{"source":16,"begin":14201,"end":14205},{"source":16,"begin":14198,"end":14199},{"source":16,"begin":14191,"end":14206},{"source":16,"begin":14225,"end":14229},{"source":16,"begin":14222,"end":14223},{"source":16,"begin":14215,"end":14230}]}}
		AssignExpCmd lastHasThrown!!276:80 false
		AssignExpCmd lastReverted!!277:13 true
		AnnotationCmd JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Revert","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":100,"charByteOffset":17},"end":{"line":100,"charByteOffset":54}}}}
		LabelCmd "End procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
		JumpCmd 4_0_0_0_0_0
	}
	Block 4_0_0_1_0_3825 Succ [4_0_0_0_0_0] {
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6104,"bytecodeCount":11,"sources":[{"source":7,"begin":5331,"end":5389}]}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25497,"bytecodeCount":18,"sources":[{"source":16,"begin":23438,"end":23857},{"source":16,"begin":23604,"end":23608},{"source":16,"begin":23642,"end":23644},{"source":16,"begin":23631,"end":23640},{"source":16,"begin":23627,"end":23645},{"source":16,"begin":23619,"end":23645},{"source":16,"begin":23691,"end":23700},{"source":16,"begin":23685,"end":23689},{"source":16,"begin":23681,"end":23701},{"source":16,"begin":23677,"end":23678},{"source":16,"begin":23666,"end":23675},{"source":16,"begin":23662,"end":23679},{"source":16,"begin":23655,"end":23702},{"source":16,"begin":23719,"end":23850},{"source":16,"begin":23845,"end":23849}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25463,"bytecodeCount":7,"sources":[{"source":16,"begin":23066,"end":23432},{"source":16,"begin":23208,"end":23211},{"source":16,"begin":23229,"end":23296},{"source":16,"begin":23293,"end":23295},{"source":16,"begin":23288,"end":23291}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22601,"bytecodeCount":15,"sources":[{"source":16,"begin":1623,"end":1792},{"source":16,"begin":1707,"end":1718},{"source":16,"begin":1741,"end":1747},{"source":16,"begin":1736,"end":1739},{"source":16,"begin":1729,"end":1748},{"source":16,"begin":1781,"end":1785},{"source":16,"begin":1776,"end":1779},{"source":16,"begin":1772,"end":1786},{"source":16,"begin":1757,"end":1786}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25475,"bytecodeCount":7,"sources":[{"source":16,"begin":23229,"end":23296},{"source":16,"begin":23222,"end":23296},{"source":16,"begin":23305,"end":23398},{"source":16,"begin":23394,"end":23397}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25423,"bytecodeCount":8,"sources":[{"source":16,"begin":22885,"end":23060},{"source":16,"begin":23025,"end":23052},{"source":16,"begin":23021,"end":23022},{"source":16,"begin":23013,"end":23019},{"source":16,"begin":23009,"end":23023},{"source":16,"begin":23002,"end":23053}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25486,"bytecodeCount":10,"sources":[{"source":16,"begin":23305,"end":23398},{"source":16,"begin":23423,"end":23425},{"source":16,"begin":23418,"end":23421},{"source":16,"begin":23414,"end":23426},{"source":16,"begin":23407,"end":23426},{"source":16,"begin":23066,"end":23432}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25520,"bytecodeCount":7,"sources":[{"source":16,"begin":23719,"end":23850},{"source":16,"begin":23711,"end":23850},{"source":16,"begin":23438,"end":23857}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":6153,"bytecodeCount":8,"sources":[{"source":7,"begin":5331,"end":5389}]}}
		AssignExpCmd lastHasThrown!!278:80 false
		AssignExpCmd lastReverted!!279:13 true
		AnnotationCmd JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Revert","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":101,"charByteOffset":8},"end":{"line":101,"charByteOffset":66}}}}
		LabelCmd "End procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
		JumpCmd 4_0_0_0_0_0
	}
	Block 4_0_0_1_0_3826 Succ [4_0_0_0_0_0] {
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9517,"bytecodeCount":11,"sources":[{"source":7,"begin":22023,"end":22078}]}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25497,"bytecodeCount":18,"sources":[{"source":16,"begin":23438,"end":23857},{"source":16,"begin":23604,"end":23608},{"source":16,"begin":23642,"end":23644},{"source":16,"begin":23631,"end":23640},{"source":16,"begin":23627,"end":23645},{"source":16,"begin":23619,"end":23645},{"source":16,"begin":23691,"end":23700},{"source":16,"begin":23685,"end":23689},{"source":16,"begin":23681,"end":23701},{"source":16,"begin":23677,"end":23678},{"source":16,"begin":23666,"end":23675},{"source":16,"begin":23662,"end":23679},{"source":16,"begin":23655,"end":23702},{"source":16,"begin":23719,"end":23850},{"source":16,"begin":23845,"end":23849}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25463,"bytecodeCount":7,"sources":[{"source":16,"begin":23066,"end":23432},{"source":16,"begin":23208,"end":23211},{"source":16,"begin":23229,"end":23296},{"source":16,"begin":23293,"end":23295},{"source":16,"begin":23288,"end":23291}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22601,"bytecodeCount":15,"sources":[{"source":16,"begin":1623,"end":1792},{"source":16,"begin":1707,"end":1718},{"source":16,"begin":1741,"end":1747},{"source":16,"begin":1736,"end":1739},{"source":16,"begin":1729,"end":1748},{"source":16,"begin":1781,"end":1785},{"source":16,"begin":1776,"end":1779},{"source":16,"begin":1772,"end":1786},{"source":16,"begin":1757,"end":1786}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25475,"bytecodeCount":7,"sources":[{"source":16,"begin":23229,"end":23296},{"source":16,"begin":23222,"end":23296},{"source":16,"begin":23305,"end":23398},{"source":16,"begin":23394,"end":23397}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25423,"bytecodeCount":8,"sources":[{"source":16,"begin":22885,"end":23060},{"source":16,"begin":23025,"end":23052},{"source":16,"begin":23021,"end":23022},{"source":16,"begin":23013,"end":23019},{"source":16,"begin":23009,"end":23023},{"source":16,"begin":23002,"end":23053}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25486,"bytecodeCount":10,"sources":[{"source":16,"begin":23305,"end":23398},{"source":16,"begin":23423,"end":23425},{"source":16,"begin":23418,"end":23421},{"source":16,"begin":23414,"end":23426},{"source":16,"begin":23407,"end":23426},{"source":16,"begin":23066,"end":23432}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":25520,"bytecodeCount":7,"sources":[{"source":16,"begin":23719,"end":23850},{"source":16,"begin":23711,"end":23850},{"source":16,"begin":23438,"end":23857}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9566,"bytecodeCount":8,"sources":[{"source":7,"begin":22023,"end":22078}]}}
		AssignExpCmd lastHasThrown!!280:80 false
		AssignExpCmd lastReverted!!281:13 true
		AnnotationCmd JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Revert","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":287,"charByteOffset":8},"end":{"line":287,"charByteOffset":63}}}}
		LabelCmd "End procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
		JumpCmd 4_0_0_0_0_0
	}
	Block 4_0_0_1_0_3827 Succ [4_0_0_0_0_0] {
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15302,"bytecodeCount":3,"sources":[{"source":7,"begin":21525,"end":21562}]}}
		AnnotationCmd JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":24261,"bytecodeCount":10,"sources":[{"source":16,"begin":14056,"end":14236},{"source":16,"begin":14104,"end":14181},{"source":16,"begin":14101,"end":14102},{"source":16,"begin":14094,"end":14182},{"source":16,"begin":14201,"end":14205},{"source":16,"begin":14198,"end":14199},{"source":16,"begin":14191,"end":14206},{"source":16,"begin":14225,"end":14229},{"source":16,"begin":14222,"end":14223},{"source":16,"begin":14215,"end":14230}]}}
		AssignExpCmd lastHasThrown!!282:80 false
		AssignExpCmd lastReverted!!283:13 true
		AnnotationCmd JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Revert","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}}}}
		LabelCmd "End procedure ERC3525-approve(uint256,address,uint256)"
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"8cb0a511"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
		JumpCmd 4_0_0_0_0_0
	}
}
Axioms {
}
Metas {
  "0": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM0x20",
        "maybeTACKeywordOrdinal": 38
      }
    },
    {
      "key": {
        "name": "tac.is.reserved.memory.slot.var",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "20"
    }
  ],
  "1": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM0x40",
        "maybeTACKeywordOrdinal": 39
      }
    },
    {
      "key": {
        "name": "tac.is.reserved.memory.slot.var",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "40"
    }
  ],
  "2": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "3": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCodesize",
        "maybeTACKeywordOrdinal": 7
      }
    },
    {
      "key": {
        "name": "tac.codesize",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "4": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacNonce",
        "maybeTACKeywordOrdinal": 44
      }
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "5": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 1,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "6": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "24"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "24"
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "24"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "7": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "44"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "44"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "44"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "8": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "3"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "3"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_tokenIdGenerator"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "3"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "9": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacContractsCreated",
        "maybeTACKeywordOrdinal": 46
      }
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "10": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacAddress",
        "maybeTACKeywordOrdinal": 22
      }
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    }
  ],
  "11": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "7"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "7"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "12": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "13": [
    {
      "key": {
        "name": "tac.last.reverted",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastReverted"
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "lastReverted"
    }
  ],
  "14": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    }
  ],
  "15": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "1"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "1"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "16": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        },
        "offset": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "17": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                    "slot": "4"
                  }
                },
                "offset": "0"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "4"
              }
            },
            "offset": "0"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "18": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM0x0",
        "maybeTACKeywordOrdinal": 37
      }
    },
    {
      "key": {
        "name": "tac.is.reserved.memory.slot.var",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "0"
    }
  ],
  "19": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacExtcodesize",
        "maybeTACKeywordOrdinal": 25
      }
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.is.extcodesize",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "20": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "6"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "6"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "21": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacS",
        "maybeTACKeywordOrdinal": 2
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "22": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                    "slot": "5"
                  }
                },
                "offset": "5"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "5"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "23": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "3"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        },
        "offset": "3"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "24": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "2"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        },
        "offset": "2"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "25": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "4"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        },
        "offset": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "26": [
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "27": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatasize",
        "maybeTACKeywordOrdinal": 12
      }
    }
  ],
  "28": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                    "slot": "7"
                  }
                },
                "offset": "0"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "7"
              }
            },
            "offset": "0"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "29": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacT",
        "maybeTACKeywordOrdinal": 5
      }
    },
    {
      "key": {
        "name": "tac.transient_storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    }
  ],
  "30": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "31": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "32": [
    {
      "key": {
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM",
        "maybeTACKeywordOrdinal": 1
      }
    },
    {
      "key": {
        "name": "tac.memory.partition",
        "type": "analysis.pta.abi.UnindexedPartition",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "id": 0
      }
    }
  ],
  "33": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacBalance",
        "maybeTACKeywordOrdinal": 23
      }
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "34": [
    {
      "key": {
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM",
        "maybeTACKeywordOrdinal": 1
      }
    },
    {
      "key": {
        "name": "tacsimplesimple.havocme",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.memory.partition",
        "type": "analysis.pta.abi.UnindexedPartition",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "id": 0
      }
    }
  ],
  "35": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "1"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        },
        "offset": "1"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "36": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                    "slot": "7"
                  }
                },
                "offset": "1"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "7"
              }
            },
            "offset": "1"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "37": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    }
  ],
  "38": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    }
  ],
  "39": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    }
  ],
  "40": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "2"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "2"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_decimals"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 8
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "2"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "41": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 1,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "42": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1011
    }
  ],
  "43": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1010
    }
  ],
  "44": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1010
    }
  ],
  "45": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "ecrecover"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "1"
    }
  ],
  "46": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "sha256"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "2"
    }
  ],
  "47": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "identity"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "4"
    }
  ],
  "48": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "ERC3525"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "49": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    }
  ],
  "50": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "1"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    }
  ],
  "51": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "3"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    }
  ],
  "52": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    }
  ],
  "53": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "2"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 8
      }
    }
  ],
  "54": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "8"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    }
  ],
  "55": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1011
    }
  ],
  "56": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1008
    }
  ],
  "57": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    }
  ],
  "58": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    }
  ],
  "59": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    }
  ],
  "60": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    }
  ],
  "61": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
      }
    }
  ],
  "62": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1013
    }
  ],
  "63": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1005
    }
  ],
  "64": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1005
    }
  ],
  "65": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1004
    }
  ],
  "66": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1004
    }
  ],
  "67": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1007
    }
  ],
  "68": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1007
    }
  ],
  "69": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1008
    }
  ],
  "70": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1013
    }
  ],
  "71": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "72": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1012
    }
  ],
  "73": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1014
    }
  ],
  "74": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1015
    }
  ],
  "75": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1018
    }
  ],
  "76": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1017
    }
  ],
  "77": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1003
    }
  ],
  "78": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1002
    }
  ],
  "79": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1001
    }
  ],
  "80": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastHasThrown"
      }
    },
    {
      "key": {
        "name": "tac.last.has.thrown",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "lastHasThrown"
    }
  ],
  "81": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "82": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "1"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "1"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "1"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "83": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                    "slot": "7"
                  }
                },
                "offset": "2"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "7"
              }
            },
            "offset": "2"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "84": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "8"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "8"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "metadataDescriptor"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "8"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "85": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "msg",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "msg",
              "fields": [
                {
                  "fieldName": "sender",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "value",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "sender",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.msg.sender"
    }
  ],
  "86": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "msg",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "msg",
              "fields": [
                {
                  "fieldName": "sender",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "value",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "value",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.msg.value"
    }
  ],
  "87": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "tx",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "tx",
              "fields": [
                {
                  "fieldName": "origin",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "origin",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.tx.origin"
    }
  ],
  "88": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "basefee",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.block.basefee"
    }
  ],
  "89": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "blobbasefee",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.block.blobbasefee"
    }
  ],
  "90": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "coinbase",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.block.coinbase"
    }
  ],
  "91": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "difficulty",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.block.difficulty"
    }
  ],
  "92": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "gaslimit",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.block.gaslimit"
    }
  ],
  "93": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "number",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.block.number"
    }
  ],
  "94": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "timestamp",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 118,
            "charByteOffset": 4
          },
          "end": {
            "line": 118,
            "charByteOffset": 10
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "e.block.timestamp"
    }
  ],
  "95": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 119,
            "charByteOffset": 4
          },
          "end": {
            "line": 119,
            "charByteOffset": 20
          }
        }
      }
    },
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "zeroAddr"
    }
  ],
  "96": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 120,
            "charByteOffset": 4
          },
          "end": {
            "line": 120,
            "charByteOffset": 17
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "value"
    }
  ],
  "97": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "id",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "98": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "owner",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON20",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1014
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON20",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1014
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "60"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1015
    }
  ],
  "99": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "id",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON35",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1003
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON35",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1003
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1004
    }
  ],
  "100": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "owner",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON47",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON47",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "60"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1010
    }
  ],
  "101": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1013
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "102": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1007
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "103": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "id",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON76",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1002
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON76",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1002
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1003
    }
  ],
  "104": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "approved",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON88",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON88",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "80"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "105": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract",
        "name": {
          "name": "ERC3525"
        }
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "currentContract"
    }
  ],
  "106": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    }
  ],
  "107": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "1"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    }
  ],
  "108": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "3"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    }
  ],
  "109": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    }
  ],
  "110": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "2"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 8
      }
    }
  ],
  "111": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "8"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
      }
    }
  ],
  "112": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
      }
    }
  ],
  "113": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastStorage"
      }
    }
  ],
  "114": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacSighash",
        "maybeTACKeywordOrdinal": 6
      }
    }
  ],
  "115": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "specs/ERC3525.spec",
          "start": {
            "line": 117,
            "charByteOffset": 29
          },
          "end": {
            "line": 117,
            "charByteOffset": 44
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "tokenId"
    }
  ],
  "116": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 0
    }
  ],
  "117": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1
    }
  ],
  "118": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 2
    }
  ],
  "119": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 3
    }
  ],
  "120": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "ERC3525"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "121": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 4
    }
  ],
  "122": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 5
    }
  ],
  "123": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 6
    }
  ],
  "124": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "125": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCodesize",
        "maybeTACKeywordOrdinal": 7
      }
    },
    {
      "key": {
        "name": "tac.codesize",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "126": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 7
    }
  ],
  "127": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    }
  ],
  "128": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 9
    }
  ],
  "129": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 10
    }
  ],
  "130": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 11
    }
  ],
  "131": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 12
    }
  ],
  "132": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 13
    }
  ],
  "133": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 14
    }
  ],
  "134": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 15
    }
  ],
  "135": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 16
    }
  ],
  "136": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 17
    }
  ],
  "137": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 18
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 118,
          "charByteOffset": 4
        },
        "end": {
          "line": 118,
          "charByteOffset": 10
        }
      }
    }
  ],
  "138": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 118,
          "charByteOffset": 4
        },
        "end": {
          "line": 118,
          "charByteOffset": 10
        }
      }
    }
  ],
  "139": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 19
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 119,
          "charByteOffset": 4
        },
        "end": {
          "line": 119,
          "charByteOffset": 66
        }
      }
    }
  ],
  "140": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "0",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "0"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "specs/ERC3525.spec",
              "start": {
                "line": 119,
                "charByteOffset": 23
              },
              "end": {
                "line": 119,
                "charByteOffset": 65
              }
            }
          },
          "printHint": "16"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 119,
          "charByteOffset": 4
        },
        "end": {
          "line": 119,
          "charByteOffset": 66
        }
      }
    }
  ],
  "141": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 119,
          "charByteOffset": 4
        },
        "end": {
          "line": 119,
          "charByteOffset": 66
        }
      }
    }
  ],
  "142": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 20
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 120,
          "charByteOffset": 4
        },
        "end": {
          "line": 120,
          "charByteOffset": 24
        }
      }
    }
  ],
  "143": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "64",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "64"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "specs/ERC3525.spec",
              "start": {
                "line": 120,
                "charByteOffset": 20
              },
              "end": {
                "line": 120,
                "charByteOffset": 23
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 120,
          "charByteOffset": 4
        },
        "end": {
          "line": 120,
          "charByteOffset": 24
        }
      }
    }
  ],
  "144": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 120,
          "charByteOffset": 4
        },
        "end": {
          "line": 120,
          "charByteOffset": 24
        }
      }
    }
  ],
  "145": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 21
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "146": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "tokenId",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "specs/ERC3525.spec",
              "start": {
                "line": 122,
                "charByteOffset": 26
              },
              "end": {
                "line": 122,
                "charByteOffset": 33
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "147": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "zeroAddr",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "specs/ERC3525.spec",
              "start": {
                "line": 122,
                "charByteOffset": 35
              },
              "end": {
                "line": 122,
                "charByteOffset": 43
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "148": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "value",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "specs/ERC3525.spec",
              "start": {
                "line": 122,
                "charByteOffset": 45
              },
              "end": {
                "line": 122,
                "charByteOffset": 50
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "149": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON71",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "150": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "151": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON75",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "152": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "I41",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "153": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "154": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "0",
        "tag": {
          "#class": "tac.Tag.Int"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "155": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "64",
        "tag": {
          "#class": "tac.Tag.Int"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "156": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON83",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "157": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON85",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "158": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON86",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "159": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON87",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "160": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON88",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "161": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON89",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "162": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON90",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "163": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON91",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "164": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON92",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "165": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON93",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "166": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON94",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "167": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON96",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "168": [
    {
      "key": {
        "name": "tac.transfers.balance",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "169": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacAddress",
        "maybeTACKeywordOrdinal": 22
      }
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "ERC3525"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "170": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 589,
        "len": 47643,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "171": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9047,
        "len": 849,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "172": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 16,
        "begin": 3035,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "173": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!76",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "174": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 16,
        "begin": 4229,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "175": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9527,
        "len": 25,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "176": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5128,
        "len": 24,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "177": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 22031,
        "len": 17,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "178": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1008
    }
  ],
  "179": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21499,
        "len": 78,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "180": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.is.revert.management",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "181": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 22
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 124,
          "charByteOffset": 4
        },
        "end": {
          "line": 124,
          "charByteOffset": 67
        }
      }
    }
  ],
  "182": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "lastReverted",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "specs/ERC3525.spec",
              "start": {
                "line": 124,
                "charByteOffset": 11
              },
              "end": {
                "line": 124,
                "charByteOffset": 23
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 124,
          "charByteOffset": 4
        },
        "end": {
          "line": 124,
          "charByteOffset": 67
        }
      }
    }
  ],
  "183": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 124,
          "charByteOffset": 4
        },
        "end": {
          "line": 124,
          "charByteOffset": 67
        }
      }
    }
  ],
  "184": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 23
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 117,
          "charByteOffset": 0
        },
        "end": {
          "line": 125,
          "charByteOffset": 1
        }
      }
    }
  ],
  "185": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
          "b": "0",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Empty"
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 117,
          "charByteOffset": 0
        },
        "end": {
          "line": 125,
          "charByteOffset": 1
        }
      }
    }
  ],
  "186": [
    {
      "key": {
        "name": "cvl.user.defined.assert",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 117,
          "charByteOffset": 0
        },
        "end": {
          "line": 125,
          "charByteOffset": 1
        }
      }
    }
  ],
  "187": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 15913,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "188": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 15913,
        "len": 46,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "189": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 15913,
        "len": 46,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "4"
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "190": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "approved",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R177",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R177",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "80"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "191": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 15417,
        "len": 549,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "192": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1013
    }
  ],
  "193": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5171,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "194": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5171,
        "len": 43,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "195": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5171,
        "len": 43,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "3"
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "196": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "owner",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R184",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R184",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "60"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1010
    }
  ],
  "197": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5331,
        "len": 58,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "198": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "owner",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R191",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1014
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R191",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1014
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "60"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1015
    }
  ],
  "199": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 4670,
        "len": 726,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "200": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1012
    }
  ],
  "201": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 19970,
        "len": 76,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "202": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9668,
        "len": 59,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "203": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9765,
        "len": 12,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "204": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 656,
        "len": 370,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "205": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9746,
        "len": 42,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "206": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 19808,
        "len": 25,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "207": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1003
    }
  ],
  "208": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9738,
        "len": 104,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "209": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9738,
        "len": 104,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "210": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 9853,
        "len": 36,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "211": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 35121,
        "len": 72,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "212": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 35121,
        "len": 72,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "213": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 22023,
        "len": 55,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "214": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21590,
        "len": 495,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "215": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 15924,
        "len": 25,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "216": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!3",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "217": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 15924,
        "len": 25,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "6"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "218": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R93",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "vc.data.TACSymbol$Var$KeywordEntry",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                    "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                    "name": "L",
                    "maybeTACKeywordOrdinal": 45
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1011
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "uint256",
              "numBytes": "20",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                "bitwidth": 256
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_allTokensIndex"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "6"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R93",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R174",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R175",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1008
    }
  ],
  "219": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1007
    }
  ],
  "220": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5182,
        "len": 25,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "221": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5182,
        "len": 25,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "6"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "222": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R93",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "vc.data.TACSymbol$Var$KeywordEntry",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                    "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                    "name": "L",
                    "maybeTACKeywordOrdinal": 45
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1011
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "uint256",
              "numBytes": "20",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                "bitwidth": 256
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_allTokensIndex"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "6"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R93",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R181",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R182",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "223": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R93",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "vc.data.TACSymbol$Var$KeywordEntry",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                    "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                    "name": "L",
                    "maybeTACKeywordOrdinal": 45
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1011
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "uint256",
              "numBytes": "20",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                "bitwidth": 256
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_allTokensIndex"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "6"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R93",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R188",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R189",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1014
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1014
    }
  ],
  "224": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1013
    }
  ],
  "225": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 20004,
        "len": 42,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "226": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 16977,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "227": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM0x0",
        "maybeTACKeywordOrdinal": 37
      }
    },
    {
      "key": {
        "name": "tac.is.reserved.memory.slot.var",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "0"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1007
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "228": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 16977,
        "len": 30,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "229": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 16977,
        "len": 41,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "230": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM0x0",
        "maybeTACKeywordOrdinal": 37
      }
    },
    {
      "key": {
        "name": "tac.is.reserved.memory.slot.var",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "0"
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1007
    }
  ],
  "231": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM0x20",
        "maybeTACKeywordOrdinal": 38
      }
    },
    {
      "key": {
        "name": "tac.is.reserved.memory.slot.var",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "20"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "232": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 16977,
        "len": 41,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                    "slot": "7"
                  }
                },
                "offset": "2"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "233": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R79",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "vc.data.TACSymbol$Var$KeywordEntry",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                    "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                    "name": "L",
                    "maybeTACKeywordOrdinal": 45
                  }
                },
                {
                  "key": {
                    "name": "tac.is-temp-var",
                    "type": "tac.MetaMap$Companion$NothingValue",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1007
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "address",
              "numBytes": "14",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.FieldAccess",
              "field": "approvals",
              "base": {
                "#class": "analysis.storage.DisplayPath.MapAccess",
                "key": {
                  "#class": "vc.data.TACSymbol.Var.Full",
                  "namePrefix": "R148",
                  "tag": {
                    "#class": "tac.Tag.Bit256"
                  },
                  "callIndex": 0,
                  "meta": [
                    {
                      "key": {
                        "name": "Tac.symbol.keyword",
                        "type": "vc.data.TACSymbol$Var$KeywordEntry",
                        "erasureStrategy": "Canonical"
                      },
                      "value": {
                        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                        "name": "L",
                        "maybeTACKeywordOrdinal": 45
                      }
                    },
                    {
                      "key": {
                        "name": "tac.stack.height",
                        "type": "java.lang.Integer",
                        "erasureStrategy": "Canonical"
                      },
                      "value": 1007
                    }
                  ]
                },
                "keyTyp": {
                  "#class": "tac.TACStorageType.IntegralType",
                  "typeLabel": "address",
                  "numBytes": "14",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                  },
                  "lowerBound": null,
                  "upperBound": null
                },
                "base": {
                  "#class": "analysis.storage.DisplayPath.Root",
                  "name": "_addressData"
                }
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                    "slot": "7"
                  },
                  "key": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "R148",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 0,
                    "meta": [
                      {
                        "key": {
                          "name": "Tac.symbol.keyword",
                          "type": "vc.data.TACSymbol$Var$KeywordEntry",
                          "erasureStrategy": "Canonical"
                        },
                        "value": {
                          "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                          "name": "L",
                          "maybeTACKeywordOrdinal": 45
                        }
                      },
                      {
                        "key": {
                          "name": "tac.stack.height",
                          "type": "java.lang.Integer",
                          "erasureStrategy": "Canonical"
                        },
                        "value": 1007
                      }
                    ]
                  },
                  "baseSlot": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "R199",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 0,
                    "meta": [
                      {
                        "key": {
                          "name": "tac.is-temp-var",
                          "type": "tac.MetaMap$Companion$NothingValue",
                          "erasureStrategy": "Canonical"
                        },
                        "value": {
                        }
                      }
                    ]
                  },
                  "hashResult": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "R200",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 0,
                    "meta": [
                      {
                        "key": {
                          "name": "Tac.symbol.keyword",
                          "type": "vc.data.TACSymbol$Var$KeywordEntry",
                          "erasureStrategy": "Canonical"
                        },
                        "value": {
                          "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                          "name": "L",
                          "maybeTACKeywordOrdinal": 45
                        }
                      },
                      {
                        "key": {
                          "name": "tac.is-temp-var",
                          "type": "tac.MetaMap$Companion$NothingValue",
                          "erasureStrategy": "Canonical"
                        },
                        "value": {
                        }
                      },
                      {
                        "key": {
                          "name": "tac.stack.height",
                          "type": "java.lang.Integer",
                          "erasureStrategy": "Canonical"
                        },
                        "value": 1009
                      }
                    ]
                  }
                },
                "offset": {
                  "#class": "analysis.storage.StorageAnalysis.Offset.Words",
                  "numWords": "2"
                }
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R79",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1007
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R202",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R208",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "234": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 16495,
        "len": 530,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "235": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 19970,
        "len": 134,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "236": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 20062,
        "len": 29,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "237": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 15872,
        "len": 24,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "238": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1002
    }
  ],
  "239": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 19321,
        "len": 800,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "240": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21536,
        "len": 25,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "241": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21536,
        "len": 25,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "6"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "242": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R93",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "vc.data.TACSymbol$Var$KeywordEntry",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                    "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                    "name": "L",
                    "maybeTACKeywordOrdinal": 45
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1011
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "uint256",
              "numBytes": "20",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                "bitwidth": 256
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_allTokensIndex"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "6"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R93",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R229",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R230",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1002
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1002
    }
  ],
  "243": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1001
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "244": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21525,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ],
  "245": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R93",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "vc.data.TACSymbol$Var$KeywordEntry",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                    "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                    "name": "L",
                    "maybeTACKeywordOrdinal": 45
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1011
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "uint256",
              "numBytes": "20",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                "bitwidth": 256
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_allTokensIndex"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "6"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R93",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R236",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R237",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1003
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1003
    }
  ],
  "246": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1002
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "247": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R93",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "vc.data.TACSymbol$Var$KeywordEntry",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                    "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                    "name": "L",
                    "maybeTACKeywordOrdinal": 45
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1011
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "uint256",
              "numBytes": "20",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                "bitwidth": 256
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_allTokensIndex"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "6"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R93",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R243",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R244",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1008
    }
  ],
  "248": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "5"
          }
        ]
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_allTokens"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000017"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1007
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "249": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21525,
        "len": 40,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "5"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "250": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "id",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R232",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1002
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R232",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1002
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1003
    }
  ],
  "251": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "id",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R239",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1003
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R239",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1003
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1004
    }
  ],
  "252": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "id",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R246",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allTokens"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "5"
              },
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R246",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1008
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "5"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "253": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21051,
        "len": 533,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilePath": {
            "0": "conf/libs/openzeppelin-contracts/contracts/utils/Context.sol",
            "1": "conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol",
            "2": "conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol",
            "3": "conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol",
            "4": "conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol",
            "5": "conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
            "6": "conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol",
            "7": "conf/src/ERC3525.sol",
            "8": "conf/src/IERC3525.sol",
            "9": "conf/src/IERC3525Receiver.sol",
            "10": "conf/src/IERC721.sol",
            "11": "conf/src/IERC721Receiver.sol",
            "12": "conf/src/extensions/IERC3525Metadata.sol",
            "13": "conf/src/extensions/IERC721Enumerable.sol",
            "14": "conf/src/extensions/IERC721Metadata.sol",
            "15": "conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "specs/ERC3525.spec",
        "start": {
          "line": 122,
          "charByteOffset": 4
        },
        "end": {
          "line": 122,
          "charByteOffset": 52
        }
      }
    }
  ]
}