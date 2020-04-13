# ChatColor —— 基于MCDR的彩色消息API
让你发送给玩家的字符串支持彩色,并且用起来很简单
> 参考spigot的ChatColor写的

## Usage - 食用方法
| 假装是常量的方法 | 功能 |
| ---- | ---- |
|BLACK()|使后面的字符串颜色变为黑色|
|DARK_BLUE()|使后面的字符串颜色变为深蓝色|
|GOLD()|使后面的字符串颜色变为金色|
|GRAY()|使后面的字符串颜色变为灰色|
|DARK_GRAY()|使后面的字符串颜色变为深灰色|
|BLUE()|使后面的字符串颜色变为蓝色|
|GREEN()|使后面的字符串颜色变为绿色|
|AQUA()|使后面的字符串颜色变为青色|
|RED()|使后面的字符串颜色变为红色|
|LIGHT_PURPLE()|使后面的字符串颜色变为亮紫色|
|YELLOW()|使后面的字符串颜色变为黄色|
|WHITE()|使后面的字符串颜色变为白色|
|MAGIC()|使后面的字符串格式变为随机字符(即不断变化的字符)|
|BOLD()|使后面的字符串加上加粗格式|
|STRIKETHROUGH()|使后面的字符串加上删除线格式|
|UNDERLINE()|使后面的字符串加上下划线格式|
|ITALIC()|使后面的字符串加上斜体格式|
|RESET()|重置后面的字符串格式和颜色|

| 真·方法 | 功能 |
| ------ | ---- |
|getByChar(code)|返回由 `code` 表示的颜色,当 `code` 不代表任何颜色/格式字符时返回None|
|stripColor(message)|返回剥离所有颜色/格式代码后的 `message`|
|getChar()|返回颜色代码标识|
|translateAlternateColorCodes(altColorChar, textToTranslate)|把 `textToTranslate` 所有 `altColorChar` 转换成颜色代码标识|

**ChatColor在 `server.talk()` 和 `server.say()` 中不生效,因为Fallen加了转义**

## Examples - 示例
#### 玩家进入发送欢迎
```
import ChatColor

on_player_joined(server, player):
  server.execute("tellraw @a {\"text\":\"" + ChatColor.GREEN() + "欢迎 " ChatColor.YELLOW() + player + ChatColor.GREEN() + " 加入游戏" + "\"}")
  server.execute("tellraw " + player + " {\"text":\"" + ChatColor.translateAlternateColorCodes("&", "&a欢迎回来, &e" + player) + "\"}")
```
