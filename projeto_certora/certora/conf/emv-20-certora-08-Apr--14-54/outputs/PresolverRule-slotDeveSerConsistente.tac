TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		safe_math_narrow_bv256:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow","returnSort":{"bits":256}}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		hash_2_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":2,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		skey_add:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Addition"}
	}
	UninterpretedFunctions {
	}
	tacM0x40@1:bv256:0
	tacM0x40@2:bv256:0
	tacCodesizeCANON0:bv256:1
	tacNonce:wordmap:2
	tacCalldatabufCANON0@1:bv256:3
	tacCalldatabufCANON0@2:bv256:4
	tacM0x0!!60:bv256:5
	tacM0x0!!74:bv256:5
	CANON38!!43:int:6
	CANON38!!89:int:6
	tacM0x40!!0:bv256:0
	tacM0x40!!1:bv256:0
	tacContractsCreated!!25:wordmap:7
	tacAddress!!47:bv256:8
	tacAddress!!96:bv256:8
	lastReverted:bool:9
	lastStorageCANON:wordmap:10
	CANON10!!8:wordmap:11
	CANON11!!9:wordmap:12
	CANON2!!26:wordmap:13
	tacM0x0!!109:bv256:5
	tacM0x0!!123:bv256:5
	tacExtcodesize!!6:wordmap:14
	CANON3!!27:wordmap:15
	CANON4!!28:wordmap:16
	CANON40!21:ghostmap(bv256*bv256*bv256->bv256):17
	tacSCANON0!!35:wordmap:18
	CANON5!!29:wordmap:19
	CANON6!!30:wordmap:20
	CANON7!!31:wordmap:21
	CANON8!!32:wordmap:22
	CANON9!!33:wordmap:23
	tacCalldatasize:bv256:24
	tacCalldatasize@1:bv256:24
	tacCalldatasize@2:bv256:24
	tacTCANON0:wordmap:25
	tacM0x0@1:bv256:5
	tacM0x0@2:bv256:5
	tacExtcodesize:wordmap:14
	tacCalldatasize!!44:bv256:24
	tacCalldatasize!!93:bv256:24
	tacBalance:wordmap:26
	tacBalance!!52:wordmap:26
	tacBalance!!56:wordmap:26
	tacBalance!!7:wordmap:26
	lastStorageCANON1:wordmap:10
	lastStorageCANON2:wordmap:10
	lastStorageCANON3:wordmap:27
	lastStorageCANON4:wordmap:28
	lastStorageCANON5:wordmap:28
	lastStorageCANON6:wordmap:10
	lastStorageCANON7:wordmap:28
	lastStorageCANON8:wordmap:29
	lastStorageCANON9:wordmap:29
	tacCalldatabuf@1:bytemap:30
	tacCalldatabuf@2:bytemap:31
	R2:bv256:1
	W5:wordmap:25
	B39:bool:32
	B40:bool:32
	B66:bool:33
	B72:bool:34
	B73:bool:35
	B80:bool:36
	I41:int
	I42:int
	I51:int:32
	I54:int:32
	I90:int
	I91:int
	R22:bv256:37
	R23:bv256:38
	R24:bv256:39
	R34:bv256:40
	R38:bv256:32
	R45:bv256:32
	R48:bv256:32
	R49:bv256:32
	R50:bv256:32
	R53:bv256:32
	R55:bv256:32
	R57:bv256:32
	R58:bv256:41
	R59:bv256:41
	R61:bv256:32
	R62:(uninterp) skey:41
	R63:bv256:32
	R64:bv256:41
	R65:bv256:33
	R67:(uninterp) skey:41
	R68:bv256:41
	R69:(uninterp) skey:42
	R70:bv256:42
	R71:bv256:42
	R75:bv256:32
	R76:(uninterp) skey:43
	R77:bv256:32
	R78:bv256:43
	R79:bv256:36
	R81:(uninterp) skey:43
	R82:bv256:43
	R83:(uninterp) skey:44
	R84:(uninterp) skey:44
	R85:bv256:44
	R86:bv256:45
	R94:bv256:32
	R97:bv256:32
	R98:bv256:32
	R99:bv256:32
	tacNonce!!3:wordmap:2
	B115:bool:33
	B121:bool:34
	B122:bool:35
	B129:bool:36
	I100:int:32
	I103:int:32
	I139:int
	I140:int
	R102:bv256:32
	R104:bv256:32
	R106:bv256:32
	R107:bv256:41
	R108:bv256:41
	R110:bv256:32
	R111:(uninterp) skey:41
	R112:bv256:32
	R113:bv256:41
	R114:bv256:33
	R116:(uninterp) skey:41
	R117:bv256:41
	R118:(uninterp) skey:42
	R119:bv256:42
	R120:bv256:42
	R124:bv256:32
	R125:(uninterp) skey:43
	R126:bv256:32
	R127:bv256:43
	R128:bv256:36
	R130:(uninterp) skey:43
	R131:bv256:43
	R132:(uninterp) skey:44
	R133:(uninterp) skey:44
	R134:bv256:44
	R135:bv256:45
	lastHasThrown!!136:bool:46
	tacAddress@1:bv256:8
	tacAddress@2:bv256:8
	lastReverted!!137:bool:9
	CANON12!!10:wordmap:47
	CANON13!!11:wordmap:48
	CANON14!!12:bv256:49
	LCANON0@1:bv256:41
	LCANON0@2:bv256:41
	LCANON1@1:bv256:41
	LCANON1@2:bv256:41
	LCANON2@1:bv256:41
	LCANON2@2:bv256:41
	LCANON3@1:bv256:41
	LCANON3@2:bv256:41
	LCANON4@1:bv256:33
	LCANON4@2:bv256:33
	LCANON5@1:bool:33
	LCANON5@2:bool:33
	LCANON6@1:bv256:41
	LCANON6@2:bv256:41
	LCANON7@1:bv256:41
	LCANON7@2:bv256:41
	LCANON8@1:bv256:42
	LCANON8@2:bv256:42
	LCANON9@1:bv256:50
	LCANON9@2:bv256:51
	CANON15!!13:bv256:52
	CANON16!!14:bv256:53
	CANON17!!15:bv256:54
	CANON10:wordmap:11
	CANON11:wordmap:12
	CANON12:wordmap:47
	CANON13:wordmap:48
	CANON14:bv256:49
	CANON15:bv256:52
	CANON16:bv256:53
	CANON17:bv256:54
	CANON18:bv256:55
	CANON19:bv256:56
	CANON20:wordmap:57
	CANON21:wordmap:58
	CANON22:wordmap:59
	CANON23:bv256:32
	CANON24:bool:32
	CANON25:bool:32
	CANON26:int:60
	CANON27:int:61
	CANON28:int:62
	CANON29:int:63
	CANON30:int:64
	CANON31:int:65
	CANON32:int:66
	CANON33:int:67
	CANON34:int:68
	CANON35:int:69
	CANON36:int
	CANON37:int
	CANON38:int:6
	CANON40:ghostmap(bv256*bv256*bv256->bv256):17
	CANON41:bv256:32
	CANON54:bv256:32
	CANON55:bv256:32
	CANON56:bv256:32
	CANON57:bv256:32
	CANON58:int:32
	CANON59:bv256:32
	CANON60:int:32
	CANON61:bv256:32
	CANON62@1:bv256:32
	CANON62@2:bv256:32
	CANON63@1:bv256:32
	CANON63@2:bv256:32
	CANON64@1:bv256:32
	CANON64@2:bv256:32
	CANON65@1:bv256:32
	CANON65@2:bv256:32
	CANON66@1:bv256:32
	CANON66@2:bv256:32
	CANON67:int
	CANON68:int
	CANON69:int:70
	CANON71:bv256:32
	CANON84:bv256:32
	CANON85:bv256:32
	CANON86:bv256:32
	CANON87:bv256:32
	CANON88:int:32
	CANON89:bv256:32
	CANON90:int:32
	CANON91:bv256:32
	CANON92:int
	CANON93:int
	CANON94:bool
	CANON18!!16:bv256:55
	CANON19!!17:bv256:56
	LCANON10@1:bv256:42
	LCANON10@2:bv256:42
	LCANON11@1:bool:34
	LCANON11@2:bool:34
	LCANON12@1:bool:35
	LCANON12@2:bool:35
	LCANON13@1:bv256:43
	LCANON13@2:bv256:43
	LCANON14@1:bv256:43
	LCANON14@2:bv256:43
	LCANON15@1:bv256:36
	LCANON15@2:bv256:36
	LCANON16@1:bool:36
	LCANON16@2:bool:36
	LCANON17@1:bv256:43
	LCANON17@2:bv256:43
	LCANON18@1:bv256:43
	LCANON18@2:bv256:43
	LCANON19@1:bv256:44
	LCANON19@2:bv256:44
	LCANON20@1:bv256:71
	LCANON20@2:bv256:72
	LCANON21@1:bv256:44
	LCANON21@2:bv256:44
	LCANON22@1:bv256:45
	LCANON22@2:bv256:45
	tacContractAtCANON1:bv256:37
	tacContractAtCANON2:bv256:38
	tacContractAtCANON3:bv256:39
	CANON69!!92:int:70
	lastHasThrown:bool:46
	tacContractsCreated:wordmap:7
	CANON69!!138:int:70
	lastReverted!!88:bool:9
	CANON1:int:73
	CANON2:wordmap:13
	CANON3:wordmap:15
	CANON4:wordmap:16
	CANON5:wordmap:19
	CANON6:wordmap:20
	CANON7:wordmap:21
	CANON8:wordmap:22
	CANON9:wordmap:23
	tacContractAtCANON:bv256:40
	CANON20!!18:wordmap:57
	CANON21!!19:wordmap:58
	CANON22!!20:wordmap:59
	tacSCANON0:wordmap:18
	tacCalldatasize!!4:bv256:24
	tacBalance!!101:wordmap:26
	tacBalance!!105:wordmap:26
	lastStorageCANON10:wordmap:10
	lastStorageCANON11:wordmap:10
	lastStorageCANON12:wordmap:10
	lastStorageCANON13:wordmap:27
	lastStorageCANON14:bv256:74
	lastStorageCANON15:bv256:75
	lastStorageCANON16:bv256:76
	lastStorageCANON17:bv256:77
	lastStorageCANON18:bv256:78
	lastStorageCANON19:bv256:79
	lastStorageCANON20:wordmap:10
	lastStorageCANON21:wordmap:10
	lastStorageCANON22:wordmap:80
	lastStorageCANON23:wordmap:81
	lastStorageCANON24:wordmap:81
	lastStorageCANON25:wordmap:81
	lastStorageCANON26:wordmap:81
	lastHasThrown!!46:bool:46
	lastHasThrown!!87:bool:46
	lastHasThrown!!95:bool:46
	CANON94!!141:bool:82
	tacSighash!!36:bv256:83
	tacSighash!!37:bv256:83
	tacSighash@1:bv256:83
	tacSighash@2:bv256:83
	CANON:int:84
}
Program {
	Block 0_0_0_0_0_0 Succ [1_0_0_1_0_0] {
		AssignHavocCmd tacM0x40!!0:0
		AssumeExpCmd Le(tacM0x40!!0:0 0x80 )
		AssignHavocCmd tacM0x40!!1:0
		AssumeExpCmd Le(tacM0x40!!1:0 0x80 )
		AssignHavocCmd R2:1
		AssumeExpCmd Ge(R2:1 0x1 )
		AssignHavocCmd tacCalldatasize!!4:24
		AssignHavocCmd tacExtcodesize!!6:14
		AssignHavocCmd tacBalance!!7:26
		AssignHavocCmd CANON10!!8:11
		AssignHavocCmd CANON11!!9:12
		AssignHavocCmd CANON12!!10:47
		AssignHavocCmd CANON13!!11:48
		AssignHavocCmd CANON14!!12:49
		AssignHavocCmd CANON15!!13:52
		AssignHavocCmd CANON16!!14:53
		AssignHavocCmd CANON17!!15:54
		AssumeExpCmd Ge(CANON17!!15:54 0x1 )
		AssignHavocCmd CANON18!!16:55
		AssignHavocCmd CANON19!!17:56
		AssignHavocCmd CANON20!!18:57
		AssignHavocCmd CANON21!!19:58
		AssignHavocCmd CANON22!!20:59
		AssignHavocCmd CANON26:60
		AssumeExpCmd LAnd(Ge(CANON26:60 0x0(int) ) Le(CANON26:60 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON27:61
		AssumeExpCmd Eq(CANON27:61 0x0(int) )
		AssignHavocCmd CANON28:62
		AssumeExpCmd LAnd(Ge(CANON28:62 0x0(int) ) Le(CANON28:62 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON29:63
		AssumeExpCmd LAnd(Ge(CANON29:63 0x0(int) ) Le(CANON29:63 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON30:64
		AssumeExpCmd LAnd(Ge(CANON30:64 0x0(int) ) Le(CANON30:64 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON31:65
		AssumeExpCmd LAnd(Ge(CANON31:65 0x0(int) ) Le(CANON31:65 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON32:66
		AssumeExpCmd LAnd(Ge(CANON32:66 0x0(int) ) Le(CANON32:66 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON33:67
		AssumeExpCmd LAnd(Ge(CANON33:67 0x0(int) ) Le(CANON33:67 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON34:68
		AssumeExpCmd LAnd(Ge(CANON34:68 0x0(int) ) Le(CANON34:68 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON35:69
		AssumeExpCmd LAnd(Ge(CANON35:69 0x0(int) ) Le(CANON35:69 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON40!21:17
		AssignHavocCmd R22:37
		AssumeExpCmd Eq(R22:37 0x1 )
		AssignHavocCmd R23:38
		AssumeExpCmd Eq(R23:38 0x2 )
		AssignHavocCmd R24:39
		AssumeExpCmd Eq(R24:39 0x4 )
		AssignHavocCmd CANON2!!26:13
		AssignHavocCmd CANON3!!27:15
		AssignHavocCmd CANON4!!28:16
		AssignHavocCmd CANON5!!29:19
		AssignHavocCmd CANON6!!30:20
		AssignHavocCmd CANON7!!31:21
		AssignHavocCmd CANON8!!32:22
		AssignHavocCmd CANON9!!33:23
		AssignHavocCmd R34:40
		AssumeExpCmd LAnd(Ge(R34:40 0x1 ) Le(R34:40 0xffffffffffffffffffffffffffffffffffffffff ) )
		AssignHavocCmd tacSCANON0!!35:18
		AssignHavocCmd tacSighash!!36:83
		AssumeExpCmd Eq(tacSighash!!36:83 0x263f3e7e )
		AssignHavocCmd tacSighash!!37:83
		AssumeExpCmd Eq(tacSighash!!37:83 0x263f3e7e )
		AnnotationCmd JSON{"key":{"name":"tac.state.extension","type":"analysis.icfg.Inliner$ExtendedStateVars","erasureStrategy":"Canonical"},"value":"rO0ABXNyACdhbmFseXNpcy5pY2ZnLklubGluZXIkRXh0ZW5kZWRTdGF0ZVZhcnOvh/MjxNFkQAIAAUwAFmluc3RhbmNlVG9FeHRlbmRlZFZhcnN0AA9MamF2YS91dGlsL01hcDt4cHNyACFkYXRhc3RydWN0dXJlcy5MaW5rZWRBcnJheUhhc2hNYXAAAAAAAAAAAQMAAkYACmxvYWRGYWN0b3JMAAloYXNoVGFibGV0AC5MZGF0YXN0cnVjdHVyZXMvYXJyYXloYXNodGFibGUvQXJyYXlIYXNoVGFibGU7eHB3CAAAAAFAAAAAc3IAFGphdmEubWF0aC5CaWdJbnRlZ2VyjPyfH6k7+x0DAAZJAAhiaXRDb3VudEkACWJpdExlbmd0aEkAE2ZpcnN0Tm9uemVyb0J5dGVOdW1JAAxsb3dlc3RTZXRCaXRJAAZzaWdudW1bAAltYWduaXR1ZGV0AAJbQnhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cP///////////////v////4AAAABdXIAAltCrPMX+AYIVOACAAB4cAAAABDORgSgAAAAAAAAAAAAAAAXeHNxAH4AA3cIAAAAAEAAAAB4eA=="}
		AnnotationCmd:85 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssignHavocCmd CANON:84
		AssumeExpCmd LAnd(Ge(CANON:84 0x0(int) ) Le(CANON:84 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":0,"index":0,"sym":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":47,"charByteOffset":28},"end":{"line":47,"charByteOffset":43}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"tokenId"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"tokenId","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":47,"charByteOffset":28},"end":{"line":47,"charByteOffset":43}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":47,"charByteOffset":28},"end":{"line":47,"charByteOffset":43}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"tokenId"}]}},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Parameter","sourceName":"tokenId"},"fields":null}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":0}
		AnnotationCmd:86 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd:87 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":2}
		AnnotationCmd:88 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AssignExpCmd CANON1:73 R34:89
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":3}
		AnnotationCmd:90 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":4}
		AnnotationCmd:91 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":5}
		AnnotationCmd:92 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming contracts in scene with non-empty bytecode have EXTCODESIZE larger than zero"}}
		AssignExpCmd R38:32 Select(tacExtcodesize!!6:14 Apply(to_skey:bif R34:89) )
		AssumeExpCmd Ge(R38:32 0x1 )
		AssumeExpCmd Eq(R38:93 R2:94 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":6}
		AnnotationCmd:95 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming address(0).code has no code deployed"}}
		AssignExpCmd B40:32 Eq(Select(tacExtcodesize!!6:14 Apply(skey_basic:bif 0x0) ) 0x0 )
		AssumeCmd B40:32
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":7}
		AnnotationCmd:96 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":8}
		AnnotationCmd:97 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":9}
		AnnotationCmd:98 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish addresses of precompiled contracts"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":10}
		AnnotationCmd:99 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":11}
		AnnotationCmd:100 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"static links"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":12}
		AnnotationCmd:101 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":13}
		AnnotationCmd:102 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":14}
		AnnotationCmd:103 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":15}
		AnnotationCmd:104 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Constrain immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":16}
		AnnotationCmd:105 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish equivalence of extension and base contract immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":17}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1}
		AnnotationCmd:106 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Declaration","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}},"cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"id":"e","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.CVLVar","id":"e8142"},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Variable"},"fields":[[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"coinbase"}],{"namePrefix":"CANON31","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.coinbase"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"basefee"}],{"namePrefix":"CANON29","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.basefee"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"timestamp"}],{"namePrefix":"CANON35","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.timestamp"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"blobbasefee"}],{"namePrefix":"CANON30","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.blobbasefee"}]},[{"#class":"tac.DataField.StructField","field":"tx"},{"#class":"tac.DataField.StructField","field":"origin"}],{"namePrefix":"CANON28","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.tx.origin"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"sender"}],{"namePrefix":"CANON26","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.sender"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"value"}],{"namePrefix":"CANON27","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.value"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"difficulty"}],{"namePrefix":"CANON32","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.difficulty"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"gaslimit"}],{"namePrefix":"CANON33","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.gaslimit"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"number"}],{"namePrefix":"CANON34","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":48,"charByteOffset":4},"end":{"line":48,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.number"}]}]}}
		AnnotationCmd:107 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":18}
		AnnotationCmd:108 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":50,"charByteOffset":4},"end":{"line":50,"charByteOffset":43}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":50,"charByteOffset":4},"end":{"line":50,"charByteOffset":21}},"id":"slotAntes","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":50,"charByteOffset":4},"end":{"line":50,"charByteOffset":21}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"263f3e7e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":50,"charByteOffset":31},"end":{"line":50,"charByteOffset":32}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"tokenId","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":50,"charByteOffset":34},"end":{"line":50,"charByteOffset":41}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"range":{"#class":"utils.Range.Empty","comment":"empty storage type"}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":50,"charByteOffset":24},"end":{"line":50,"charByteOffset":42}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"263f3e7e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false,"virtual":false},"stateMutability":"view","evmExternalMethodInfo":{"sigHash":"263f3e7e","name":"slotOf","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","isConstant":false,"paramNames":["tokenId_"],"isLibrary":false,"contractName":"ERC3525","contractInstanceId":"ce4604a0000000000000000000000017","sourceSegment":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}},"content":"function slotOf(uint256 tokenId_) public view virtual override returns (uint256) {\r\n        _requireMinted(tokenId_);\r\n        return _allTokens[_allTokensIndex[tokenId_]].slot;\r\n    }"}}},"hasEnv":true}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"certoraArg81648168"},"src":{"id":"e8142"}}}
		AssignExpCmd:109 I42 CANON:84
	}
	Block 1_0_0_1_0_0 Succ [2_0_0_0_0_0] {
		AssignHavocCmd:110 CANON38!!43:6
		AnnotationCmd:110 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"263f3e7e"},"attr":{"#class":"scene.MethodAttribute.Common"}},"summary":null,"convention":{"#class":"analysis.icfg.Inliner.CallConventionType.FromCVL"},"calleeId":1}}
		AssignHavocCmd:110 tacCalldatasize!!44:24
		AssumeExpCmd Eq(tacCalldatasize!!44:24 0x24 )
		AssignExpCmd:110 tacCalldatabuf@1:30 MapDefinition(CANON39.19200:bv256 -> Ite(Lt(CANON39.19200 tacCalldatasize!!44:24 ) Select(Select(Select(CANON40!21:17 CANON39.19200 ) tacCalldatasize!!44:24 ) 0x263f3e7e ) 0x0 ) bytemap)
		AssignExpCmd:110 R45:32 Select(Select(Select(CANON40!21:17 0x0 ) 0x24 ) 0x263f3e7e )
		AssumeExpCmd LAnd(Ge(R45:32 0x263f3e7e00000000000000000000000000000000000000000000000000000000 ) Le(R45:32 0x263f3e7effffffffffffffffffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd:110 JSON{"key":{"name":"cvl.arg-serialization.start","type":"spec.CVLInvocationCompiler$StartSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":1}}
		LabelCmd:110 "9: Read primitive from certoraArg81898191:int..."
		AssertCmd:111 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:111 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:110 tacCalldatabufCANON0@1:112 Apply(safe_math_narrow_bv256:bif I42)
		LabelCmd:110 "...done 9"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I42","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"0","callId":1,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"fields":null}}
		AnnotationCmd:110 JSON{"key":{"name":"cvl.arg-serialization.end","type":"spec.CVLInvocationCompiler$EndSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":1}}
		AssignExpCmd:110 lastHasThrown!!46:46 false
		AssertCmd:113 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:114 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:115 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:116 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:117 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:118 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:119 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:120 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:121 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:122 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:123 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:124 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:110 R48:32 Apply(safe_math_narrow_bv256:bif CANON26:60)
		AssignExpCmd:110 R50:32 Select(tacBalance!!7:26 Apply(to_skey:bif R48:32) )
		AssignExpCmd:125 tacBalance!!52:26 Store(tacBalance!!7:26 Apply(to_skey:bif R48:32) R50:32 )
		AssignExpCmd:110 R53:32 Select(tacBalance!!52:26 Apply(to_skey:bif R34:89) )
		AssignExpCmd:125 R55:32 Apply(safe_math_narrow_bv256:bif R53:32)
		AssignExpCmd:125 tacBalance!!56:26 Store(tacBalance!!52:26 Apply(to_skey:bif R34:89) R55:32 )
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.TransferSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R48","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R53","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R55","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"tacContractAt"}},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC3525"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Const","value":"0"}}}
		LabelCmd:110 "Start procedure ERC3525-slotOf(uint256)"
		AnnotationCmd:110 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:110 R57:32 Select(tacExtcodesize!!6:14 Apply(to_skey:bif R34:126) )
		AssumeExpCmd Ge(R57:32 0x1 )
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacAddress","maybeTACKeywordOrdinal":22}},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC3525"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]},"contractInstance":"ce4604a0000000000000000000000017","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R57","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"storageType":null,"range":null}}
		AnnotationCmd:110 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":{"unresolvedFunctions":[]}}
		AnnotationCmd:110 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":0,"bytecodeCount":8,"sources":[{"source":7,"begin":605,"end":48872}]}}
		LabelCmd "→ Assuming FP is strictly monotonic increasing"
		LabelCmd "←"
		AnnotationCmd:127 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":13,"bytecodeCount":9,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:127 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":208,"bytecodeCount":6,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:127 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":220,"bytecodeCount":5,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:127 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":279,"bytecodeCount":6,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:127 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":291,"bytecodeCount":5,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:127 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":302,"bytecodeCount":5,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:127 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":756,"bytecodeCount":6,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":0,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}},"content":"compiler-generate condition in function slotOf(uint256 tokenId_) public view virtual override returns (uint256) "}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":0}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":767,"bytecodeCount":15,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22786,"bytecodeCount":10,"sources":[{"source":16,"begin":3109,"end":3438},{"source":16,"begin":3168,"end":3174},{"source":16,"begin":3217,"end":3219},{"source":16,"begin":3205,"end":3214},{"source":16,"begin":3196,"end":3203},{"source":16,"begin":3192,"end":3215},{"source":16,"begin":3188,"end":3220},{"source":16,"begin":3185,"end":3304}]}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":1,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}},"content":"compiler-generate condition in function slotOf(uint256 tokenId_) public view virtual override returns (uint256) "}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":1}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22807,"bytecodeCount":9,"sources":[{"source":16,"begin":3185,"end":3304},{"source":16,"begin":3343,"end":3344},{"source":16,"begin":3368,"end":3421},{"source":16,"begin":3413,"end":3420},{"source":16,"begin":3404,"end":3410},{"source":16,"begin":3393,"end":3402},{"source":16,"begin":3389,"end":3411}]}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22766,"bytecodeCount":10,"sources":[{"source":16,"begin":2964,"end":3103},{"source":16,"begin":3010,"end":3015},{"source":16,"begin":3048,"end":3054},{"source":16,"begin":3035,"end":3055},{"source":16,"begin":3026,"end":3055},{"source":16,"begin":3064,"end":3097},{"source":16,"begin":3091,"end":3096}]}}
		AssignExpCmd:130 R58:41 tacCalldatabufCANON0@1:131
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22744,"bytecodeCount":5,"sources":[{"source":16,"begin":2836,"end":2958},{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2927,"end":2932}]}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22735,"bytecodeCount":9,"sources":[{"source":16,"begin":2753,"end":2830},{"source":16,"begin":2790,"end":2797},{"source":16,"begin":2819,"end":2824},{"source":16,"begin":2808,"end":2824}]}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22753,"bytecodeCount":5,"sources":[{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2902,"end":2907},{"source":16,"begin":2899,"end":2934},{"source":16,"begin":2889,"end":2952}]}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22763,"bytecodeCount":3,"sources":[{"source":16,"begin":2889,"end":2952},{"source":16,"begin":2836,"end":2958}]}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22780,"bytecodeCount":6,"sources":[{"source":16,"begin":3064,"end":3097},{"source":16,"begin":2964,"end":3103}]}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22820,"bytecodeCount":9,"sources":[{"source":16,"begin":3368,"end":3421},{"source":16,"begin":3358,"end":3421},{"source":16,"begin":3314,"end":3431},{"source":16,"begin":3109,"end":3438}]}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":789,"bytecodeCount":3,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:110 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":4484,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":5506,"len":543,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":4484,"bytecodeCount":18,"sources":[{"source":7,"begin":5506,"end":6049},{"source":7,"begin":5578,"end":5585},{"source":7,"begin":5690,"end":5703},{"source":7,"begin":5622,"end":5688},{"source":7,"begin":5615,"end":5704},{"source":7,"begin":5780,"end":5781},{"source":7,"begin":5712,"end":5778},{"source":7,"begin":5705,"end":5782},{"source":7,"begin":5858,"end":5859},{"source":7,"begin":5790,"end":5856},{"source":7,"begin":5783,"end":5860},{"source":7,"begin":5936,"end":5944},{"source":7,"begin":5868,"end":5934},{"source":7,"begin":5861,"end":5945},{"source":7,"begin":5957,"end":5981},{"source":7,"begin":5972,"end":5980},{"source":7,"begin":5957,"end":5971}]}}
		AnnotationCmd:110 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":9356,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":5957,"len":24,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:132 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9356,"bytecodeCount":17,"sources":[{"source":7,"begin":21876,"end":22373},{"source":7,"begin":22043,"end":22056},{"source":7,"begin":21975,"end":22041},{"source":7,"begin":21968,"end":22057},{"source":7,"begin":22133,"end":22134},{"source":7,"begin":22065,"end":22131},{"source":7,"begin":22058,"end":22135},{"source":7,"begin":22211,"end":22212},{"source":7,"begin":22143,"end":22209},{"source":7,"begin":22136,"end":22213},{"source":7,"begin":22289,"end":22297},{"source":7,"begin":22221,"end":22287},{"source":7,"begin":22214,"end":22298},{"source":7,"begin":22318,"end":22335},{"source":7,"begin":22326,"end":22334},{"source":7,"begin":22318,"end":22325}]}}
		AnnotationCmd:110 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":15108,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":22318,"len":17,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:133 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15108,"bytecodeCount":26,"sources":[{"source":7,"begin":21333,"end":21868},{"source":7,"begin":21399,"end":21403},{"source":7,"begin":21508,"end":21521},{"source":7,"begin":21440,"end":21506},{"source":7,"begin":21433,"end":21522},{"source":7,"begin":21598,"end":21599},{"source":7,"begin":21530,"end":21596},{"source":7,"begin":21523,"end":21600},{"source":7,"begin":21676,"end":21677},{"source":7,"begin":21608,"end":21674},{"source":7,"begin":21601,"end":21678},{"source":7,"begin":21754,"end":21762},{"source":7,"begin":21686,"end":21752},{"source":7,"begin":21679,"end":21763},{"source":7,"begin":21803,"end":21804},{"source":7,"begin":21782,"end":21792},{"source":7,"begin":21782,"end":21799},{"source":7,"begin":21782,"end":21804},{"source":7,"begin":21782,"end":21860}]}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!15","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":32}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":2,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":93}},"content":"_allTokens.length != 0 && _allTokens[_allTokensIndex[tokenId_]].id == tokenId_"}}}
		AnnotationCmd:134 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15272,"bytecodeCount":24,"sources":[{"source":7,"begin":21782,"end":21860},{"source":7,"begin":21852,"end":21860},{"source":7,"begin":21808,"end":21818},{"source":7,"begin":21819,"end":21834},{"source":7,"begin":21819,"end":21844},{"source":7,"begin":21835,"end":21843},{"source":7,"begin":21808,"end":21845}]}}
		AssignExpCmd:110 R61:32 0x6
		AssignExpCmd:135 R62:41 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:136) Apply(skey_basic:bif 0x6))
		AssignExpCmd:137 R64:41 AnnotationExp(Select(CANON3!!27:15 R62:138 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R62","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AssumeExpCmd Le(R64:41 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe )
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R64","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!44","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":52},"end":{"line":283,"charByteOffset":77}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!15","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssumeExpCmd Lt(R64:41 CANON17!!15:139 )
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":3,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":3}}
		AnnotationCmd:140 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15310,"bytecodeCount":15,"sources":[{"source":7,"begin":21808,"end":21845},{"source":7,"begin":21808,"end":21848},{"source":7,"begin":21808,"end":21860}]}}
		AssignExpCmd:140 R67:41 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:140 R68:41 Mul(0x6 R64:41 )
		AssignExpCmd:140 R69:42 Apply(skey_add:bif R67:41 R68:41)
		AssignExpCmd:141 R71:42 AnnotationExp(Select(CANON11!!9:12 R69:142 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R64","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R71","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"id","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R64","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":81}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssumeExpCmd Eq(R71:42 tacCalldatabufCANON0@1:136 )
		AnnotationCmd:110 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		LabelCmd:110 "Parallel assignment for R143:bv256 := R163:bv256"
		AnnotationCmd:110 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		AnnotationCmd:110 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		LabelCmd:110 "Parallel assignment for R66:bv256 := R64:bv256"
		AnnotationCmd:110 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":2}}
		AnnotationCmd:110 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15327,"bytecodeCount":7,"sources":[{"source":7,"begin":21782,"end":21860},{"source":7,"begin":21775,"end":21860},{"source":7,"begin":21333,"end":21868}]}}
		AssignExpCmd:110 B73:35 true
		AnnotationCmd:110 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"B73","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.was.replaced.with.bool","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9512,"bytecodeCount":3,"sources":[{"source":7,"begin":22318,"end":22335},{"source":7,"begin":22310,"end":22365}]}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":4,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":287,"charByteOffset":8},"end":{"line":287,"charByteOffset":63}},"content":"require(_exists(tokenId_), \\\"ERC3525: invalid token ID\\\")"}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":4}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9575,"bytecodeCount":3,"sources":[{"source":7,"begin":22310,"end":22365},{"source":7,"begin":21876,"end":22373}]}}
		AnnotationCmd:110 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]}}}
		AnnotationCmd:145 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":4641,"bytecodeCount":23,"sources":[{"source":7,"begin":5957,"end":5981},{"source":7,"begin":5999,"end":6009},{"source":7,"begin":6010,"end":6025},{"source":7,"begin":6010,"end":6035},{"source":7,"begin":6026,"end":6034},{"source":7,"begin":5999,"end":6036}]}}
		AssignExpCmd:110 R75:32 0x6
		AssignExpCmd:146 R76:43 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@1:136) Apply(skey_basic:bif 0x6))
		AssignExpCmd:147 R78:43 AnnotationExp(Select(CANON3!!27:15 R76:148 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R76","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AssumeExpCmd Le(R78:43 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe )
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R78","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":1,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!44","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":26},"end":{"line":106,"charByteOffset":51}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!15","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":15},"end":{"line":106,"charByteOffset":52}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssumeExpCmd Lt(R78:43 CANON17!!15:139 )
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":5,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":15},"end":{"line":106,"charByteOffset":52}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":5}}
		AnnotationCmd:149 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":4678,"bytecodeCount":20,"sources":[{"source":7,"begin":5999,"end":6036},{"source":7,"begin":5999,"end":6041},{"source":7,"begin":5992,"end":6041},{"source":7,"begin":5506,"end":6049}]}}
		AssignExpCmd:149 R81:43 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:149 R82:43 Mul(0x6 R78:43 )
		AssignExpCmd:149 R83:44 Apply(skey_add:bif R81:43 R82:43)
		AssignExpCmd:150 R84:44 Apply(skey_add:bif R83:44 0x1)
		AssignExpCmd:151 R85:44 AnnotationExp(Select(CANON21!!19:58 R84:152 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R78","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"1"}}]}})
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R85","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"slot","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R78","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":15},"end":{"line":106,"charByteOffset":57}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:110 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R85","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:153 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":794,"bytecodeCount":8,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23116,"bytecodeCount":14,"sources":[{"source":16,"begin":5532,"end":5754},{"source":16,"begin":5625,"end":5629},{"source":16,"begin":5663,"end":5665},{"source":16,"begin":5652,"end":5661},{"source":16,"begin":5648,"end":5666},{"source":16,"begin":5640,"end":5666},{"source":16,"begin":5676,"end":5747},{"source":16,"begin":5744,"end":5745},{"source":16,"begin":5733,"end":5742},{"source":16,"begin":5729,"end":5746},{"source":16,"begin":5720,"end":5726}]}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23101,"bytecodeCount":5,"sources":[{"source":16,"begin":5408,"end":5526},{"source":16,"begin":5495,"end":5519},{"source":16,"begin":5513,"end":5518}]}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22735,"bytecodeCount":9,"sources":[{"source":16,"begin":2753,"end":2830},{"source":16,"begin":2790,"end":2797},{"source":16,"begin":2819,"end":2824},{"source":16,"begin":2808,"end":2824}]}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23110,"bytecodeCount":6,"sources":[{"source":16,"begin":5495,"end":5519},{"source":16,"begin":5490,"end":5493},{"source":16,"begin":5483,"end":5520},{"source":16,"begin":5408,"end":5526}]}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R85","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23135,"bytecodeCount":6,"sources":[{"source":16,"begin":5676,"end":5747},{"source":16,"begin":5532,"end":5754}]}}
		AnnotationCmd:129 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":807,"bytecodeCount":8,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AssignExpCmd:128 lastHasThrown!!87:46 false
		AssignExpCmd:128 lastReverted!!88:9 false
		AnnotationCmd:128 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Return","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}}}}
		LabelCmd:110 "End procedure ERC3525-slotOf(uint256)"
		LabelCmd:110 "3: Move primitive value for variable slotAntes8154:int..."
		AssignExpCmd:110 CANON38!!89:6 R85:44
		LabelCmd:110 "...done 3"
		AnnotationCmd:110 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"263f3e7e"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
	}
	Block 2_0_0_0_0_0 Succ [3_0_0_2_0_0] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:110 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":19}
		AnnotationCmd:154 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":52,"charByteOffset":4},"end":{"line":52,"charByteOffset":44}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":52,"charByteOffset":4},"end":{"line":52,"charByteOffset":22}},"id":"slotDepois","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":52,"charByteOffset":4},"end":{"line":52,"charByteOffset":22}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"263f3e7e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":52,"charByteOffset":32},"end":{"line":52,"charByteOffset":33}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"tokenId","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":52,"charByteOffset":35},"end":{"line":52,"charByteOffset":42}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"range":{"#class":"utils.Range.Empty","comment":"empty storage type"}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":52,"charByteOffset":25},"end":{"line":52,"charByteOffset":43}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"263f3e7e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false,"virtual":false},"stateMutability":"view","evmExternalMethodInfo":{"sigHash":"263f3e7e","name":"slotOf","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","isConstant":false,"paramNames":["tokenId_"],"isLibrary":false,"contractName":"ERC3525","contractInstanceId":"ce4604a0000000000000000000000017","sourceSegment":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}},"content":"function slotOf(uint256 tokenId_) public view virtual override returns (uint256) {\r\n        _requireMinted(tokenId_);\r\n        return _allTokens[_allTokensIndex[tokenId_]].slot;\r\n    }"}}},"hasEnv":true}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"certoraArg91319132"},"src":{"id":"e8142"}}}
		AssignExpCmd:155 I91 CANON:84
	}
	Block 3_0_0_2_0_0 Succ [4_0_0_0_0_0] {
		AssignHavocCmd:156 CANON69!!92:70
		AnnotationCmd:156 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"263f3e7e"},"attr":{"#class":"scene.MethodAttribute.Common"}},"summary":null,"convention":{"#class":"analysis.icfg.Inliner.CallConventionType.FromCVL"},"calleeId":2}}
		AssignHavocCmd:156 tacCalldatasize!!93:24
		AssumeExpCmd Eq(tacCalldatasize!!93:24 0x24 )
		AssignExpCmd:156 tacCalldatabuf@2:31 MapDefinition(CANON70.19201:bv256 -> Ite(Lt(CANON70.19201 tacCalldatasize!!93:24 ) Select(Select(Select(CANON40!21:17 CANON70.19201 ) tacCalldatasize!!93:24 ) 0x263f3e7e ) 0x0 ) bytemap)
		AssignExpCmd:156 R94:32 Select(Select(Select(CANON40!21:17 0x0 ) 0x24 ) 0x263f3e7e )
		AssumeExpCmd LAnd(Ge(R94:32 0x263f3e7e00000000000000000000000000000000000000000000000000000000 ) Le(R94:32 0x263f3e7effffffffffffffffffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd:156 JSON{"key":{"name":"cvl.arg-serialization.start","type":"spec.CVLInvocationCompiler$StartSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":1,"callId":2}}
		LabelCmd:156 "19: Read primitive from certoraArg91339134:int..."
		AssertCmd:157 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:157 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:156 tacCalldatabufCANON0@2:112 Apply(safe_math_narrow_bv256:bif I91)
		LabelCmd:156 "...done 19"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I91","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"0","callId":2,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"fields":null}}
		AnnotationCmd:156 JSON{"key":{"name":"cvl.arg-serialization.end","type":"spec.CVLInvocationCompiler$EndSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":1,"callId":2}}
		AssignExpCmd:156 lastHasThrown!!95:46 false
		AssertCmd:158 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:159 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:160 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:161 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:162 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:163 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:164 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:165 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:166 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:167 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:168 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:169 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:156 R97:32 Apply(safe_math_narrow_bv256:bif CANON26:60)
		AssignExpCmd:156 R99:32 Select(tacBalance!!56:26 Apply(to_skey:bif R97:32) )
		AssignExpCmd:170 tacBalance!!101:26 Store(tacBalance!!56:26 Apply(to_skey:bif R97:32) R99:32 )
		AssignExpCmd:156 R102:32 Select(tacBalance!!101:26 Apply(to_skey:bif R34:89) )
		AssignExpCmd:170 R104:32 Apply(safe_math_narrow_bv256:bif R102:32)
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.TransferSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R99","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R99","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R97","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R102","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R104","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"tacContractAt"}},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC3525"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Const","value":"0"}}}
		LabelCmd:156 "Start procedure ERC3525-slotOf(uint256)"
		AnnotationCmd:156 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:156 R106:32 Select(tacExtcodesize!!6:14 Apply(to_skey:bif R34:126) )
		AssumeExpCmd Ge(R106:32 0x1 )
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacAddress","maybeTACKeywordOrdinal":22}},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC3525"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]},"contractInstance":"ce4604a0000000000000000000000017","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R106","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"storageType":null,"range":null}}
		AnnotationCmd:156 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":{"unresolvedFunctions":[]}}
		AnnotationCmd:156 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":0,"bytecodeCount":8,"sources":[{"source":7,"begin":605,"end":48872}]}}
		LabelCmd "→ Assuming FP is strictly monotonic increasing"
		LabelCmd "←"
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":13,"bytecodeCount":9,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":208,"bytecodeCount":6,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":220,"bytecodeCount":5,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":279,"bytecodeCount":6,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":291,"bytecodeCount":5,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":302,"bytecodeCount":5,"sources":[{"source":7,"begin":605,"end":48872}]}}
		AnnotationCmd:171 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":756,"bytecodeCount":6,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":6,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}},"content":"compiler-generate condition in function slotOf(uint256 tokenId_) public view virtual override returns (uint256) "}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":6}}
		AnnotationCmd:172 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":767,"bytecodeCount":15,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22786,"bytecodeCount":10,"sources":[{"source":16,"begin":3109,"end":3438},{"source":16,"begin":3168,"end":3174},{"source":16,"begin":3217,"end":3219},{"source":16,"begin":3205,"end":3214},{"source":16,"begin":3196,"end":3203},{"source":16,"begin":3192,"end":3215},{"source":16,"begin":3188,"end":3220},{"source":16,"begin":3185,"end":3304}]}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":7,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}},"content":"compiler-generate condition in function slotOf(uint256 tokenId_) public view virtual override returns (uint256) "}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":7}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22807,"bytecodeCount":9,"sources":[{"source":16,"begin":3185,"end":3304},{"source":16,"begin":3343,"end":3344},{"source":16,"begin":3368,"end":3421},{"source":16,"begin":3413,"end":3420},{"source":16,"begin":3404,"end":3410},{"source":16,"begin":3393,"end":3402},{"source":16,"begin":3389,"end":3411}]}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22766,"bytecodeCount":10,"sources":[{"source":16,"begin":2964,"end":3103},{"source":16,"begin":3010,"end":3015},{"source":16,"begin":3048,"end":3054},{"source":16,"begin":3035,"end":3055},{"source":16,"begin":3026,"end":3055},{"source":16,"begin":3064,"end":3097},{"source":16,"begin":3091,"end":3096}]}}
		AssignExpCmd:174 R107:41 tacCalldatabufCANON0@2:175
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22744,"bytecodeCount":5,"sources":[{"source":16,"begin":2836,"end":2958},{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2927,"end":2932}]}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22735,"bytecodeCount":9,"sources":[{"source":16,"begin":2753,"end":2830},{"source":16,"begin":2790,"end":2797},{"source":16,"begin":2819,"end":2824},{"source":16,"begin":2808,"end":2824}]}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22753,"bytecodeCount":5,"sources":[{"source":16,"begin":2909,"end":2933},{"source":16,"begin":2902,"end":2907},{"source":16,"begin":2899,"end":2934},{"source":16,"begin":2889,"end":2952}]}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22763,"bytecodeCount":3,"sources":[{"source":16,"begin":2889,"end":2952},{"source":16,"begin":2836,"end":2958}]}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22780,"bytecodeCount":6,"sources":[{"source":16,"begin":3064,"end":3097},{"source":16,"begin":2964,"end":3103}]}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22820,"bytecodeCount":9,"sources":[{"source":16,"begin":3368,"end":3421},{"source":16,"begin":3358,"end":3421},{"source":16,"begin":3314,"end":3431},{"source":16,"begin":3109,"end":3438}]}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":789,"bytecodeCount":3,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:156 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":4484,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R107","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":5506,"len":543,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":4484,"bytecodeCount":18,"sources":[{"source":7,"begin":5506,"end":6049},{"source":7,"begin":5578,"end":5585},{"source":7,"begin":5690,"end":5703},{"source":7,"begin":5622,"end":5688},{"source":7,"begin":5615,"end":5704},{"source":7,"begin":5780,"end":5781},{"source":7,"begin":5712,"end":5778},{"source":7,"begin":5705,"end":5782},{"source":7,"begin":5858,"end":5859},{"source":7,"begin":5790,"end":5856},{"source":7,"begin":5783,"end":5860},{"source":7,"begin":5936,"end":5944},{"source":7,"begin":5868,"end":5934},{"source":7,"begin":5861,"end":5945},{"source":7,"begin":5957,"end":5981},{"source":7,"begin":5972,"end":5980},{"source":7,"begin":5957,"end":5971}]}}
		AnnotationCmd:156 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":9356,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R107","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":5957,"len":24,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:176 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9356,"bytecodeCount":17,"sources":[{"source":7,"begin":21876,"end":22373},{"source":7,"begin":22043,"end":22056},{"source":7,"begin":21975,"end":22041},{"source":7,"begin":21968,"end":22057},{"source":7,"begin":22133,"end":22134},{"source":7,"begin":22065,"end":22131},{"source":7,"begin":22058,"end":22135},{"source":7,"begin":22211,"end":22212},{"source":7,"begin":22143,"end":22209},{"source":7,"begin":22136,"end":22213},{"source":7,"begin":22289,"end":22297},{"source":7,"begin":22221,"end":22287},{"source":7,"begin":22214,"end":22298},{"source":7,"begin":22318,"end":22335},{"source":7,"begin":22326,"end":22334},{"source":7,"begin":22318,"end":22325}]}}
		AnnotationCmd:156 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":15108,"args":[{"s":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R107","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"logicalPosition":0,"sort":"SCALAR","location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":7,"begin":22318,"len":17,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilePath":{"0":"conf/libs/openzeppelin-contracts/contracts/utils/Context.sol","1":"conf/libs/openzeppelin-contracts/contracts/utils/Panic.sol","2":"conf/libs/openzeppelin-contracts/contracts/utils/Strings.sol","3":"conf/libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol","4":"conf/libs/openzeppelin-contracts/contracts/utils/math/Math.sol","5":"conf/libs/openzeppelin-contracts/contracts/utils/math/SafeCast.sol","6":"conf/libs/openzeppelin-contracts/contracts/utils/math/SignedMath.sol","7":"conf/src/ERC3525.sol","8":"conf/src/IERC3525.sol","9":"conf/src/IERC3525Receiver.sol","10":"conf/src/IERC721.sol","11":"conf/src/IERC721Receiver.sol","12":"conf/src/extensions/IERC3525Metadata.sol","13":"conf/src/extensions/IERC721Enumerable.sol","14":"conf/src/extensions/IERC721Metadata.sol","15":"conf/src/periphery/interface/IERC3525MetadataDescriptor.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:177 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15108,"bytecodeCount":26,"sources":[{"source":7,"begin":21333,"end":21868},{"source":7,"begin":21399,"end":21403},{"source":7,"begin":21508,"end":21521},{"source":7,"begin":21440,"end":21506},{"source":7,"begin":21433,"end":21522},{"source":7,"begin":21598,"end":21599},{"source":7,"begin":21530,"end":21596},{"source":7,"begin":21523,"end":21600},{"source":7,"begin":21676,"end":21677},{"source":7,"begin":21608,"end":21674},{"source":7,"begin":21601,"end":21678},{"source":7,"begin":21754,"end":21762},{"source":7,"begin":21686,"end":21752},{"source":7,"begin":21679,"end":21763},{"source":7,"begin":21803,"end":21804},{"source":7,"begin":21782,"end":21792},{"source":7,"begin":21782,"end":21799},{"source":7,"begin":21782,"end":21804},{"source":7,"begin":21782,"end":21860}]}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!15","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":32}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":8,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":15},"end":{"line":283,"charByteOffset":93}},"content":"_allTokens.length != 0 && _allTokens[_allTokensIndex[tokenId_]].id == tokenId_"}}}
		AnnotationCmd:178 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15272,"bytecodeCount":24,"sources":[{"source":7,"begin":21782,"end":21860},{"source":7,"begin":21852,"end":21860},{"source":7,"begin":21808,"end":21818},{"source":7,"begin":21819,"end":21834},{"source":7,"begin":21819,"end":21844},{"source":7,"begin":21835,"end":21843},{"source":7,"begin":21808,"end":21845}]}}
		AssignExpCmd:156 R110:32 0x6
		AssignExpCmd:179 R111:41 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@2:136) Apply(skey_basic:bif 0x6))
		AssignExpCmd:180 R113:41 AnnotationExp(Select(CANON3!!27:15 R111:181 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R107","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R111","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AssumeExpCmd Le(R113:41 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe )
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R113","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":2,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":52},"end":{"line":283,"charByteOffset":77}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!15","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssumeExpCmd Lt(R113:41 CANON17!!15:139 )
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":9,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":78}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":9}}
		AnnotationCmd:182 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15310,"bytecodeCount":15,"sources":[{"source":7,"begin":21808,"end":21845},{"source":7,"begin":21808,"end":21848},{"source":7,"begin":21808,"end":21860}]}}
		AssignExpCmd:182 R116:41 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:182 R117:41 Mul(0x6 R113:41 )
		AssignExpCmd:182 R118:42 Apply(skey_add:bif R116:41 R117:41)
		AssignExpCmd:183 R120:42 AnnotationExp(Select(CANON11!!9:12 R118:184 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R113","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R120","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"id","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R113","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":283,"charByteOffset":41},"end":{"line":283,"charByteOffset":81}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssumeExpCmd Eq(R120:42 tacCalldatabufCANON0@2:136 )
		AnnotationCmd:156 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		LabelCmd:156 "Parallel assignment for R143:bv256 := R163:bv256"
		AnnotationCmd:156 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		AnnotationCmd:156 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		LabelCmd:156 "Parallel assignment for R66:bv256 := R64:bv256"
		AnnotationCmd:156 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"15310_1013_0_0_0_0 -> 15327_1015_0_0_0_0"}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":8}}
		AnnotationCmd:156 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":15327,"bytecodeCount":7,"sources":[{"source":7,"begin":21782,"end":21860},{"source":7,"begin":21775,"end":21860},{"source":7,"begin":21333,"end":21868}]}}
		AssignExpCmd:156 B122:35 true
		AnnotationCmd:156 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"B122","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.was.replaced.with.bool","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_exists"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:185 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9512,"bytecodeCount":3,"sources":[{"source":7,"begin":22318,"end":22335},{"source":7,"begin":22310,"end":22365}]}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":10,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":287,"charByteOffset":8},"end":{"line":287,"charByteOffset":63}},"content":"require(_exists(tokenId_), \\\"ERC3525: invalid token ID\\\")"}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":10}}
		AnnotationCmd:186 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":9575,"bytecodeCount":3,"sources":[{"source":7,"begin":22310,"end":22365},{"source":7,"begin":21876,"end":22373}]}}
		AnnotationCmd:156 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"_requireMinted"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]}}}
		AnnotationCmd:187 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":4641,"bytecodeCount":23,"sources":[{"source":7,"begin":5957,"end":5981},{"source":7,"begin":5999,"end":6009},{"source":7,"begin":6010,"end":6025},{"source":7,"begin":6010,"end":6035},{"source":7,"begin":6026,"end":6034},{"source":7,"begin":5999,"end":6036}]}}
		AssignExpCmd:156 R124:32 0x6
		AssignExpCmd:188 R125:43 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@2:136) Apply(skey_basic:bif 0x6))
		AssignExpCmd:189 R127:43 AnnotationExp(Select(CANON3!!27:15 R125:190 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"6"},"key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R107","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"6"},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R125","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AssumeExpCmd Le(R127:43 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe )
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatabufCANON0","tag":{"#class":"tac.Tag.Bit256"},"callIndex":2,"meta":[{"key":{"name":"tac.immutable.array","type":"vc.data.ImmutableBound","erasureStrategy":"Canonical"},"value":{"sym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"tacCalldatasize!!93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatasize","maybeTACKeywordOrdinal":12}}]}}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacCalldatabuf","maybeTACKeywordOrdinal":15}},{"key":{"name":"tac.wordmap-key","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"4"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.calldata.offset","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"4"},{"key":{"name":"tac.is.calldata","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokensIndex"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":26},"end":{"line":106,"charByteOffset":51}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON17!!15","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":15},"end":{"line":106,"charByteOffset":52}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssumeExpCmd Lt(R127:43 CANON17!!15:139 )
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":11,"branchSource":{"range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":15},"end":{"line":106,"charByteOffset":52}},"content":"_allTokens[_allTokensIndex[tokenId_]]"}}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":11}}
		AnnotationCmd:191 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":4678,"bytecodeCount":20,"sources":[{"source":7,"begin":5999,"end":6036},{"source":7,"begin":5999,"end":6041},{"source":7,"begin":5992,"end":6041},{"source":7,"begin":5506,"end":6049}]}}
		AssignExpCmd:191 R130:43 Apply(hash_2_keccak:bif Apply(skey_basic:bif 0x20) Apply(skey_basic:bif 0x5))
		AssignExpCmd:191 R131:43 Mul(0x6 R127:43 )
		AssignExpCmd:191 R132:44 Apply(skey_add:bif R130:43 R131:43)
		AssignExpCmd:192 R133:44 Apply(skey_add:bif R132:44 0x1)
		AssignExpCmd:193 R134:44 AnnotationExp(Select(CANON21!!19:58 R133:194 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.ArrayAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"5"},"index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"5"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"1"}}]}})
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R134","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"slot","base":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allTokens"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":106,"charByteOffset":15},"end":{"line":106,"charByteOffset":57}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":1}}}
		AnnotationCmd:156 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"R134","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC3525"},"methodId":"slotOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"tokenId_","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:195 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":794,"bytecodeCount":8,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23116,"bytecodeCount":14,"sources":[{"source":16,"begin":5532,"end":5754},{"source":16,"begin":5625,"end":5629},{"source":16,"begin":5663,"end":5665},{"source":16,"begin":5652,"end":5661},{"source":16,"begin":5648,"end":5666},{"source":16,"begin":5640,"end":5666},{"source":16,"begin":5676,"end":5747},{"source":16,"begin":5744,"end":5745},{"source":16,"begin":5733,"end":5742},{"source":16,"begin":5729,"end":5746},{"source":16,"begin":5720,"end":5726}]}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23101,"bytecodeCount":5,"sources":[{"source":16,"begin":5408,"end":5526},{"source":16,"begin":5495,"end":5519},{"source":16,"begin":5513,"end":5518}]}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":22735,"bytecodeCount":9,"sources":[{"source":16,"begin":2753,"end":2830},{"source":16,"begin":2790,"end":2797},{"source":16,"begin":2819,"end":2824},{"source":16,"begin":2808,"end":2824}]}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23110,"bytecodeCount":6,"sources":[{"source":16,"begin":5495,"end":5519},{"source":16,"begin":5490,"end":5493},{"source":16,"begin":5483,"end":5520},{"source":16,"begin":5408,"end":5526}]}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R134","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":23135,"bytecodeCount":6,"sources":[{"source":16,"begin":5676,"end":5747},{"source":16,"begin":5532,"end":5754}]}}
		AnnotationCmd:173 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"ERC3525","contractAddress":"ce4604a0000000000000000000000017","contractBytecodeHash":"59b4321e4310b06cd3dbd5b7f6d36a222a5e89f0835c861dae3cd8533fc6014a","pc":807,"bytecodeCount":8,"sources":[{"source":7,"begin":5506,"end":6049}]}}
		AssignExpCmd:172 lastHasThrown!!136:46 false
		AssignExpCmd:172 lastReverted!!137:9 false
		AnnotationCmd:172 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:156 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Return","range":{"specFile":"conf/src/ERC3525.sol","start":{"line":104,"charByteOffset":4},"end":{"line":107,"charByteOffset":5}}}}
		LabelCmd:156 "End procedure ERC3525-slotOf(uint256)"
		LabelCmd:156 "16: Move primitive value for variable slotDepois9130:int..."
		AssignExpCmd:156 CANON69!!138:70 R134:44
		LabelCmd:156 "...done 16"
		AnnotationCmd:156 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000017","sigHash":{"n":"263f3e7e"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":2}}
	}
	Block 4_0_0_0_0_0 Succ [] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:156 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":20}
		AnnotationCmd:196 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":53,"charByteOffset":4},"end":{"line":53,"charByteOffset":35}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"slotAntes","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":53,"charByteOffset":11},"end":{"line":53,"charByteOffset":20}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"slotDepois","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":53,"charByteOffset":24},"end":{"line":53,"charByteOffset":34}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"specs/ERC3525.spec","start":{"line":53,"charByteOffset":11},"end":{"line":53,"charByteOffset":34}}}},"description":"slotAntes == slotDepois","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:197 I139 CANON38!!89:6
		AssignExpCmd:198 I140 CANON69!!138:70
		AssignExpCmd:199 CANON94!!141:82 Eq(I139 I140 )
		AssertCmd:200 CANON94!!141:82 "slotAntes == slotDepois"
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
  "1": [
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
  "2": [
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
  "3": [
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
  "4": [
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
          "callIndex": 2,
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
  "5": [
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
  "6": [
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
            "line": 50,
            "charByteOffset": 4
          },
          "end": {
            "line": 50,
            "charByteOffset": 21
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
      "value": "slotAntes"
    }
  ],
  "7": [
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
  "8": [
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
  "9": [
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
  "10": [
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
  "13": [
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
  "14": [
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
  "17": [
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
  "18": [
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
  "19": [
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
  "21": [
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
  "24": [
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
  "25": [
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
  "26": [
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
  "27": [
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
  "28": [
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
  "29": [
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
  "30": [
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
  "31": [
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
          "callIndex": 2,
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
  "32": [
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
  "33": [
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
  "34": [
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
  "35": [
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
      "value": 1018
    }
  ],
  "36": [
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
  "37": [
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
  "38": [
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
  "39": [
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
  "40": [
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
  "41": [
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
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1014
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
      "value": 1019
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
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1020
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
      "value": 1023
    }
  ],
  "46": [
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
  "47": [
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
  "48": [
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
  "49": [
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
  "50": [
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
                "namePrefix": "LCANON3",
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
                    "value": 1013
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
                "namePrefix": "LCANON3",
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
                    "value": 1013
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
      "value": 1014
    }
  ],
  "51": [
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
                "namePrefix": "LCANON3",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
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
                    "value": 1013
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
                "namePrefix": "LCANON3",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
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
                    "value": 1013
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
      "value": 1014
    }
  ],
  "52": [
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
  "53": [
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
  "54": [
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
  "55": [
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
  "56": [
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
  "57": [
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
  "58": [
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
  "59": [
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
  "60": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "61": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "62": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "63": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "64": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "65": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "66": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "67": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "68": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "69": [
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
            "line": 48,
            "charByteOffset": 4
          },
          "end": {
            "line": 48,
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
  "70": [
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
            "line": 52,
            "charByteOffset": 4
          },
          "end": {
            "line": 52,
            "charByteOffset": 22
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
      "value": "slotDepois"
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
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "slot",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON14",
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
                    "value": 1019
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
                "namePrefix": "LCANON14",
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
                    "value": 1019
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
              "numWords": "1"
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
      "value": 1020
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
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "slot",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "LCANON14",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
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
                    "value": 1019
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
                "namePrefix": "LCANON14",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
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
                    "value": 1019
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
              "numWords": "1"
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
      "value": 1020
    }
  ],
  "73": [
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
  "74": [
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
  "75": [
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
  "76": [
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
  "77": [
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
  "78": [
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
  "79": [
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
  "80": [
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
  "81": [
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
  "82": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "83": [
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
  "84": [
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
            "line": 47,
            "charByteOffset": 28
          },
          "end": {
            "line": 47,
            "charByteOffset": 43
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
  "85": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 0
    }
  ],
  "86": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1
    }
  ],
  "87": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 2
    }
  ],
  "88": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 3
    }
  ],
  "89": [
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
  "90": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 4
    }
  ],
  "91": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 5
    }
  ],
  "92": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 6
    }
  ],
  "93": [
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
  "94": [
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
  "95": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 7
    }
  ],
  "96": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    }
  ],
  "97": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 9
    }
  ],
  "98": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 10
    }
  ],
  "99": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 11
    }
  ],
  "100": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 12
    }
  ],
  "101": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 13
    }
  ],
  "102": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 14
    }
  ],
  "103": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 15
    }
  ],
  "104": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 16
    }
  ],
  "105": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 17
    }
  ],
  "106": [
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
          "line": 48,
          "charByteOffset": 4
        },
        "end": {
          "line": 48,
          "charByteOffset": 10
        }
      }
    }
  ],
  "107": [
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
          "line": 48,
          "charByteOffset": 4
        },
        "end": {
          "line": 48,
          "charByteOffset": 10
        }
      }
    }
  ],
  "108": [
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "109": [
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
                  "scopeId": 3
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
                "line": 50,
                "charByteOffset": 34
              },
              "end": {
                "line": 50,
                "charByteOffset": 41
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "110": [
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "111": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "I42",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "112": [
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
  "113": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON42",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "114": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON43",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "115": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON44",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "116": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON45",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "117": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON46",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "118": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON47",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "119": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON48",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "120": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON49",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "121": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON50",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "122": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON51",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "123": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON52",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "124": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON53",
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "125": [
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "126": [
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
  "127": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 605,
        "len": 48267,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "128": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5506,
        "len": 543,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "129": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5506,
        "len": 543,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "130": [
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "131": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!44",
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
  "132": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5957,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "133": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 22318,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "134": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21782,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "135": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21819,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "136": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!4",
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
  "137": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21819,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
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
  "138": [
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
              "namePrefix": "R58",
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
                  "value": 1013
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
                "namePrefix": "R58",
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
                    "value": 1013
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R61",
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
                "namePrefix": "R62",
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
                    "value": 1013
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
      "value": 1013
    }
  ],
  "139": [
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
  "140": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21808,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "141": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21808,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
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
  "142": [
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
                "namePrefix": "R64",
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
                    "value": 1013
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
                "namePrefix": "R64",
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
                    "value": 1013
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
      "value": 1014
    }
  ],
  "143": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21333,
        "len": 535,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "144": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 22310,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "145": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21876,
        "len": 497,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "146": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 6010,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "147": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 6010,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
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
  "148": [
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
              "namePrefix": "R58",
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
                  "value": 1013
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
                "namePrefix": "R58",
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
                    "value": 1013
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R75",
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
                "namePrefix": "R76",
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
                    "value": 1019
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
      "value": 1019
    }
  ],
  "149": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5999,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "150": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5999,
        "len": 42,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "151": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5999,
        "len": 42,
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
            "offset": "1"
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    },
    {
      "key": {
        "name": "tac.call-graph.address-read",
        "type": "analysis.icfg.CallGraphBuilder$ContractStorageRead",
        "erasureStrategy": "Canonical"
      },
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZJo5HPv1EkgqAgABSQACaWR4cAAAAAA="
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
  "152": [
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
            "field": "slot",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R78",
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
                    "value": 1019
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
                "namePrefix": "R78",
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
                    "value": 1019
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
              "numWords": "1"
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
      "value": 1020
    }
  ],
  "153": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5506,
        "len": 543,
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
          "line": 50,
          "charByteOffset": 4
        },
        "end": {
          "line": 50,
          "charByteOffset": 43
        }
      }
    }
  ],
  "154": [
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "155": [
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
                  "scopeId": 3
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
                "line": 52,
                "charByteOffset": 35
              },
              "end": {
                "line": 52,
                "charByteOffset": 42
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "156": [
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "I91",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON72",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON73",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON74",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON76",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON77",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON78",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON79",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON80",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "namePrefix": "CANON81",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "168": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON82",
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "169": [
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "170": [
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "begin": 605,
        "len": 48267,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "source": 7,
        "begin": 5506,
        "len": 543,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "173": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5506,
        "len": 543,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "175": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!93",
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
  "176": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5957,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "begin": 22318,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "178": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21782,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
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
        "begin": 21819,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "180": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21819,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
  "181": [
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
              "namePrefix": "R107",
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
                  "value": 1013
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
                "namePrefix": "R107",
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
                    "value": 1013
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R110",
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
                "namePrefix": "R111",
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
                    "value": 1013
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
      "value": 1013
    }
  ],
  "182": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21808,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "183": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21808,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
  "184": [
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
                "namePrefix": "R113",
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
                    "value": 1013
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
                "namePrefix": "R113",
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
                    "value": 1013
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
      "value": 1014
    }
  ],
  "185": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 21333,
        "len": 535,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "186": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 22310,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "begin": 21876,
        "len": 497,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "begin": 6010,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
        "begin": 6010,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
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
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R107",
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
                  "value": 1013
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
                "namePrefix": "R107",
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
                    "value": 1013
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R124",
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
                "namePrefix": "R125",
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
                    "value": 1019
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
      "value": 1019
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
        "begin": 5999,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "192": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5999,
        "len": 42,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
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
        "begin": 5999,
        "len": 42,
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
            "offset": "1"
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    },
    {
      "key": {
        "name": "tac.call-graph.address-read",
        "type": "analysis.icfg.CallGraphBuilder$ContractStorageRead",
        "erasureStrategy": "Canonical"
      },
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZJo5HPv1EkgqAgABSQACaWR4cAAAAAE="
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
  "194": [
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
            "field": "slot",
            "base": {
              "#class": "analysis.storage.DisplayPath.ArrayAccess",
              "index": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R127",
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
                    "value": 1019
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
                "namePrefix": "R127",
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
                    "value": 1019
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
              "numWords": "1"
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
      "value": 1020
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
        "begin": 5506,
        "len": 543,
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
          "line": 52,
          "charByteOffset": 4
        },
        "end": {
          "line": 52,
          "charByteOffset": 44
        }
      }
    }
  ],
  "196": [
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
          "line": 53,
          "charByteOffset": 4
        },
        "end": {
          "line": 53,
          "charByteOffset": 35
        }
      }
    }
  ],
  "197": [
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
          "id": "slotAntes",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 3
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
                "line": 53,
                "charByteOffset": 11
              },
              "end": {
                "line": 53,
                "charByteOffset": 20
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
          "line": 53,
          "charByteOffset": 4
        },
        "end": {
          "line": 53,
          "charByteOffset": 35
        }
      }
    }
  ],
  "198": [
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
          "id": "slotDepois",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 3
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
                "line": 53,
                "charByteOffset": 24
              },
              "end": {
                "line": 53,
                "charByteOffset": 34
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
          "line": 53,
          "charByteOffset": 4
        },
        "end": {
          "line": 53,
          "charByteOffset": 35
        }
      }
    }
  ],
  "199": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "slotAntes",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 3
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
                  "line": 53,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 53,
                  "charByteOffset": 20
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "slotDepois",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 3
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
                  "line": 53,
                  "charByteOffset": 24
                },
                "end": {
                  "line": 53,
                  "charByteOffset": 34
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 3
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
                "line": 53,
                "charByteOffset": 11
              },
              "end": {
                "line": 53,
                "charByteOffset": 34
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I139",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "slotAntes",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 3
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
                  "line": 53,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 53,
                  "charByteOffset": 20
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I140",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "slotDepois",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 3
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
                  "line": 53,
                  "charByteOffset": 24
                },
                "end": {
                  "line": 53,
                  "charByteOffset": 34
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
          "line": 53,
          "charByteOffset": 4
        },
        "end": {
          "line": 53,
          "charByteOffset": 35
        }
      }
    }
  ],
  "200": [
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
          "line": 53,
          "charByteOffset": 4
        },
        "end": {
          "line": 53,
          "charByteOffset": 35
        }
      }
    }
  ]
}