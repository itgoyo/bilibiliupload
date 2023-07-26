# 更新日志

## 标签含义
- 💡新添加的功能
- 🔧已修复的问题
- ⚠️需要手动操作的更新信息
  
## 0.4.24
- 🔧修复哔哩哔哩flv流403的问题。 [@xxxxuanran](https://github.com/xxxxuanran)
  
## 0.4.23
- 更新时间：2023.07.17
- 🔧preprocessor增加开播时返回主播名字和开播地址 [@Kataick](https://github.com/Kataick)
- 🔧修复当获取流失败后会触发获取流频繁的问题 [@Kataick](https://github.com/Kataick)
- 🔧优化设置大delay会出现漏录的问题 [@Kataick](https://github.com/Kataick)
- 🔧优化在config中读取值的代码写法 [@Kataick](https://github.com/Kataick)
- 🔧增加对yt-dlp的lazy_playlist功能支持 [@Kataick](https://github.com/Kataick)
- 🔧修复format为mp4时无法时间分段的问题 [@Kataick](https://github.com/Kataick)
- 🔧修复bilibili导致进程卡死问题(get_play_info) [@Kataick](https://github.com/Kataick)
- 🔧修复afreecaTV导致进程卡死问题 [@Kataick](https://github.com/Kataick)
- 🔧修复快手导致进程卡死问题 [@Kataick](https://github.com/Kataick)
- 🔧去除 quickjs 依赖。相对应的修改了 Readme 和 Douyu [@xxxxuanran](https://github.com/xxxxuanran)
- 🔧Bililive 兼容 `APEX分区。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧Kuaishou 新增 协议切换 和 CDN 优选。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧修正快手 HLS 流原画 [@xxxxuanran](https://github.com/xxxxuanran) 
- 🔧修复biliup-rs的参数绑定[@hguandl](https://github.com/hguandl)
- 💡增加由于地区限制导致无法下载指定区域直播间的提示。[@xxxxuanran](https://github.com/xxxxuanran)
- 💡增加对biliup-rs的支持(杜比音效、Hi-Res、转载、充电) [@Kataick](https://github.com/Kataick)
- 💡bili_web上传插件新增简介@功能 [@zzc10086](https://github.com/zzc10086)
- 💡增加抖音弹幕录制支持 [@KNaiFen](https://github.com/KNaiFen)

## 0.4.22
- 更新时间：2023.06.29
- 🔧优化虎牙错误提示和抖音代码与错误提示。[@Kataick](https://github.com/Kataick)
- 🔧优化获取直播流失败时增加等待重试。[@Kataick](https://github.com/Kataick)
- 🔧修复ffmpeg时长分段时弹幕文件不会跟着分段的问题、修复防止重复请求流的功能工作异常的问题。[@KNaiFen](https://github.com/KNaiFen)
- 🔧修正CHANGELOG更新日志、修正README.MD。[@KNaiFen](https://github.com/KNaiFen)
- 🔧弹幕报错记录增加文件名部分，方便排查BUG。[@KNaiFen](https://github.com/KNaiFen)
- 🔧yaml、toml配置文件注释修正，格式修正。[@KNaiFen](https://github.com/KNaiFen)
- 💡「BETA」增加未上传完录像时同一主播重新开播是否立刻开始录制功能。[@Kataick](https://github.com/Kataick)
- 💡「BETA」增加cn01的fmp4流获取真原画流功能。[@haha114514](https://github.com/haha114514)

## 0.4.21
- 更新时间：2023.06.11
- 🔧抖音增加获取错误时的提示并优化纯数字房间号的代码。[@Kataick](https://github.com/Kataick)
- 🔧修复虎牙与抖音关闭连接导致进程终止问题。[@Kataick](https://github.com/Kataick)
- 🔧同步yaml配置文件的更新到toml中。[@Kataick](https://github.com/Kataick)
- 🔧NICO标题获取从BS4改为正则，开播后仍然重复请求的BUG的修复。[@KNaiFen](https://github.com/KNaiFen)
- 🔧添加quickjs依赖。[@haha114514](https://github.com/haha114514)
- 💡新增NICO录播。[@KNaiFen](https://github.com/KNaiFen)
- 💡增加NICO用户配置文件模板。[@KNaiFen](https://github.com/KNaiFen)
- 💡增加Twitch的去广告开关（解决广告分段问题）[@KNaiFen](https://github.com/KNaiFen)
- 💡增加Twitch弹幕录播、修复斗鱼、虎牙的弹幕录制BUG并增加报错提示，修改了XML文件的删除部分，修改了部分代码的协程的调用，优化断流时频繁重复请求。[@KNaiFen](https://github.com/KNaiFen)

## 0.4.20
- 更新时间：2023.05.25
- 🔧修复抖音可能导致进程卡死问题。[@KkakaMann](https://github.com/KkakaMann)
- 🔧改正部分下载器的日志等级，避免刷屏。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧尝试修复斗鱼下载失败的问题，同时禁用主线路。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧修正快手日志提示，尝试规避风控。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧修正Windows下自动过滤删除文件由于占用权限问题，导致整体卡住的问题。[@haha114514](https://github.com/haha114514)

## 0.4.19
- 更新时间：2023.05.11
- 🔧修复新版本urllib3.connectionpool下xrange报错的问题。[@zclkkk](https://github.com/zclkkk)
- 🔧修复新版本urllib3 2下method_whitelist报错的问题。[@Weidows](https://github.com/Weidows)

## 0.4.18
- 更新时间：2023.04.21
- 🔧修复录制B站直播，自动上传标题里面的title为下播前的最后一个标题的bug（正确的应该是开播之后的第一个标题）。[@haha114514](https://github.com/haha114514)
- 🔧streamlink下载稳定与内存占用优化。[@haha114514](https://github.com/haha114514)
- 🔧修复多余弹幕文件自动过滤失效的问题。[@haha114514](https://github.com/haha114514)
- 🔧增加B站fmp4流的等待时间，因为有些主播开播到推流时间较慢。[@zclkkk](https://github.com/zclkkk)
- 💡B站直播优选CDN支持同时添加多个节点。[@haha114514](https://github.com/haha114514)
- 💡新增B站自定义fmp4流获取不到时，重新获取一遍flv直播流的API。[@haha114514](https://github.com/haha114514)
- 💡新增对快手平台的支持。[@xxxxuanran](https://github.com/xxxxuanran)

## 0.4.17
- 更新时间：2023.03.24
- 🔧修复不填B站自定义API就无法开始录制的问题。[@xxxxuanran](https://github.com/xxxxuanran)

## 0.4.16 ⚠️⚠️有重大问题，请勿使用该版本。
- 更新时间：2023.03.23
- 🔧修复B站自定义API不生效的问题。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧修复部分config示例的错误。[@haha114514](https://github.com/haha114514)

## 0.4.15
- 更新时间：2023.03.21
- 🔧修复上一版本关于b站下载部分的优化相关的问题。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧优化YouTube下载相关参数。[@haha114514](https://github.com/haha114514)

## 0.4.14
- 更新时间：2023.03.19
- 🔧回滚@xxxxuanran关于b站下载部分的优化。[@haha114514](https://github.com/haha114514)

## 0.4.13 ⚠️⚠️有重大问题，请勿使用该版本。
- 更新时间：2023.03.19
- 🔧优化部分下载逻辑，并将封面下载功能移动到download.py中，方便以后适配更多平台的直播间封面下载。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧修复配置文件错误。[@xxxxuanran](https://github.com/xxxxuanran)
- 🔧优化streamlink下载参数。[@haha114514](https://github.com/haha114514)
- 💡新增跳过斗鱼scdn，并增加了斗鱼与虎牙最新的CDN的支持。[@xxxxuanran](https://github.com/xxxxuanran)
- 💡新增指定YouTube视频下载时间范围区间的功能。[@haha114514](https://github.com/haha114514)
- ⚠️上一条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。

## 0.4.12
- 更新时间：2023.03.17
- 🔧修复优选CDN与直播流不生效的问题。[@haha114514](https://github.com/haha114514)
- 🔧优化streamlink下载参数。[@haha114514](https://github.com/haha114514)
- 🔧完善依赖列表,将最低的yt-dlp版本要求升级到2023.3.3，解决2022年版本已无法解析YouTube视频的问题。并且将streamlink最低要求版本升级到5.3.0，提升hls流录制稳定性。[@haha114514](https://github.com/haha114514)

## 0.4.11
- 更新时间：2023.03.07
- 🔧修复上一版本的封面上传问题。[@haha114514](https://github.com/haha114514)

## 0.4.10 ⚠️⚠️有重大问题，请勿使用该版本。
- 更新时间：2023.03.07
- 🔧修复上一版本的封面上传问题。[@haha114514](https://github.com/haha114514)
- 🔧优化上传过滤文件规则。[@haha114514](https://github.com/haha114514)
- 💡修改判断逻辑，支持cn-gotcha01 flv流的自选域名。[@haha114514](https://github.com/haha114514)
- 💡增加YouTube转载视频自动获取视频封面并用作投稿封面的功能。[@haha114514](https://github.com/haha114514)

## 0.4.9 ⚠️⚠️有重大问题，请勿使用该版本。
- 更新时间：2023.03.06
- 🔧biliup-rs上传器自动过滤xml文件，避免上传xml弹幕文件导致整个投稿转码失败的问题。[@haha114514](https://github.com/haha114514)
- 🔧修复自动获取封面不生效的问题[@haha114514](https://github.com/haha114514)

## 0.4.8
- 更新时间：2023.03.04
- 🔧在最后处理文件的时候，自动删除多余的xml弹幕文件，只保留有同样文件名视频的弹幕xml文件[@haha114514](https://github.com/haha114514)
- 🔧优化ffmpeg录制hls流的参数[@haha114514](https://github.com/haha114514)
- 💡新增streamlink+ffmpeg混合下载器选项[@haha114514](https://github.com/haha114514)
- 💡新增B站直播hls_fmp4流的获取（目前只有streamlink+ffmpeg混合模式才能稳定下载）[@haha114514](https://github.com/haha114514)
- ⚠️上两条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。

## 0.4.7 
- 更新时间：2023.02.28
- 🔧修复0.4.5的BUG并添加缺失的依赖[@haha114514](https://github.com/haha114514)

## 0.4.5 ⚠️⚠️有重大问题，请勿使用该版本。
- 更新时间：2023.02.28
- 💡新增斗鱼，虎牙，B站的弹幕录制功能，默认关闭，需要在config文件中开启，只支持FFMPEG（目前）[@KNaiFen](https://github.com/KNaiFen) （感谢：[THMonster/danmaku](https://github.com/THMonster/danmaku) ）
- 🔧修复了BILIBILI录制中OV05节点的BUG[@haha114514](https://github.com/haha114514)
- ⚠️由于为Config新增了弹幕录制的设置，如需使用相关功能请参考最新的config示例添加缺失的部分。
- 🔧优化代码[@ForgQi](https://github.com/ForgQi)

## 0.4.4 ⚠️⚠️本次修改了config内部分参数的名称，请需要使用的用户参考最新的config示例修改
-  更新时间：2023.02.20
- 💡统一了Config中关键词替换的关键词。 [@haha114514](https://github.com/haha114514)
- ⚠️⚠️请注意修改file_name与title和Description中关键词替换的部分。目前全部统一为streamer，title和url了。
- 💡新增cn-gotcha01和ov-gotcha05自选ip/节点的设置。 [@haha114514](https://github.com/haha114514)
- ⚠️上一条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。
- 🔧修复上一版本由于新增的哔哩哔哩直播自定义下载CDN导致报错的问题。 [@haha114514](https://github.com/haha114514)
- 🔧修复过多请求开播API导致IP被限制访问的问题。[@ForgQi](https://github.com/ForgQi)

## 0.4.3
-  更新时间：2023.02.15
- 💡为YouTube视频下载增加指定音视频编码的设置。 [@haha114514](https://github.com/haha114514)
- ⚠️上一条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。
- 🔧修复上一版本由于新增的哔哩哔哩直播自定义下载CDN导致报错的问题。 [@haha114514](https://github.com/haha114514)

## 0.4.2 ⚠️⚠️此版本存在重大BUG，导致很多情况下无法录制B站直播，请勿使用。
-  更新时间：2023.02.15
- 💡为YouTube视频下载增加指定封装格式，最大纵向分辨率，最大单视频大小的设置。 [@haha114514](https://github.com/haha114514)
- ⚠️上一条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。
- 🔧修复上一版本由于新增的哔哩哔哩登录Cookie导致报错的问题。 [@haha114514](https://github.com/haha114514)
- 🔧修复Twitch的Clips无法下载的问题。 [@haha114514](https://github.com/haha114514)
- 🔧为上一版本的B站Fallback机制启用开关。[@haha114514](https://github.com/haha114514)
- ⚠️上一条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。

## 0.4.1
-  更新时间：2023.02.13
- 💡增加Preprocessor功能，支持开始录制时执行指定Shell指令 [@haha114514](https://github.com/haha114514)
- 💡为上传标题与简介增加streamers变量 [@haha114514](https://github.com/haha114514)
- ⚠️上两条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。
- 🔧修复访问acfun过于频繁导致ip被拉黑之后报错卡住的问题 [@haha114514](https://github.com/haha114514)
- 🔧修复嵌入示例中延后发布时间的错误 [@stevenlele](https://github.com/setvenlele)
- 🔧修复twitch_cookie配置不生效问题 [@v2wy](https://github.com/v2wy)
- 🔧尝试为B站直播录制启用Fallback机制，当指定CDN反复无法下载之后，自动尝试另外的CDN [@xxxxuanran](https://github.com/xxxxuanran)
- 🔧增加Cookie登录B站功能，可用于下载付费直播与大航海专属直播 [@xxxxuanran](https://github.com/xxxxuanran)
- ⚠️上一条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。

## 0.4.0
-  更新时间：2023.02.10
- ⚠️修改cookie在配置文件中的位置 [@haha114514](https://github.com/haha114514)
- 🔧修复斗鱼直播间被关闭一直报错的问题 [@v2wy](https://github.com/v2wy)
- 🔧修改probe_version参数，增加两个常用的网页上传地址 [@FairyWorld](https://github.com/FairyWorld)

## 0.3.12
-  更新时间：2023.02.05
- 🔧为readme文档添加关于主要支持录制的直播平台的介绍以及删掉关于上传CDN描述中已经失效的节点 [@haha114514](https://github.com/haha114514)
- 🔧修复ffmpeg录制参数缺失.part后缀，导致录制出来的文件都没有.part后缀的问题 [@haha114514](https://github.com/haha114514)
- 🔧修复了ffmpeg录制情况下，按大小分段录制时，分段之后上一段的.part后缀不会被去掉的问题 [@haha114514](https://github.com/haha114514)
- 🔧完善config示例，增加postprocessor可参考用法的描述 [@haha114514](https://github.com/haha114514)
- ⚠️上一条由于为Config新增了一些设置，如需使用相关功能请参考最新的config示例添加缺失的部分。

## 0.3.11
-  更新时间：2023.02.02
- 🔧修复config.yaml示例中filename_prefix配置格式 [@FairyWorld](https://github.com/FairyWorld)
- 🔧添加config.toml示例中缺失的关于downloader的设置 [@haha114514](https://github.com/haha114514)
- 🔧修改postprocessor，避免出现指令有问题导致反复从头开始执行任务的问题 [@haha114514](https://github.com/haha114514)
- 🔧去掉自动替换文件名中空格为_字符的功能，避免和录播完毕自动改名冲突 [@haha114514](https://github.com/haha114514)
- 🔧修复由于上一版的修改导致stream-gears录制文件名重复出现分段覆盖的问题[@haha114514](https://github.com/haha114514)

## 0.3.10 ⚠️⚠️此版本存在stream-gears录制文件名重复导致覆盖上一段分段的问题，请勿使用
-  更新时间：2023.02.01
- 💡添加全局与单个主播自定义录播文件命名设置 [@haha114514](https://github.com/haha114514)
- ⚠️新增与主播自定义录播文件命名设置的两个参数，如需使用此功能，请老版本用户参考config的示例添加。[@haha114514](https://github.com/haha114514)
- 💡启用了文件名过滤特殊字符的功能，避免文件名中出现特殊字符，导致ffmpeg无法录制的问题。[@haha114514](https://github.com/haha114514)

## 0.3.9 
-  更新时间：2023.01.31
- 💡添加一个虎牙的CDN线路 [@ForgQi](https://github.com/ForgQi)
- 🔧虎牙无法正确获取房间标题的问题 [@luckycat0426](https://github.com/luckycat0426)
- 💡哔哩哔哩直播流协议.可选 stream（Flv）、hls [@xxxxuanran](https://github.com/xxxxuanran)
- 💡哔哩哔哩直播优选CDN [@xxxxuanran](https://github.com/xxxxuanran)
- 💡哔哩哔哩直播强制原画（仅限HLS流的 cn-gotcha01 CDN） [@xxxxuanran](https://github.com/xxxxuanran)
- 💡自定义哔哩哔哩直播API [@xxxxuanran](https://github.com/xxxxuanran)
- 💡Twitch自定义用户Cookie，作用是可以不让广告嵌入到视频流中 [@KNaiFen](https://github.com/KNaiFen)
