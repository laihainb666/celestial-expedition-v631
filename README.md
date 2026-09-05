# 苍穹远征：星陨传说（Celestial Expedition）

纯 Python 标准库实现的超大型文字 RPG，零第三方依赖。

## 版本
- **V6.3.1**（单文件整合版，内含全量游戏数据）

## 文件说明
| 文件 | 说明 |
|---|---|
| celestial_expedition_v631_singlefile.py | 单文件整合版：含全部数据，一个文件即可运行（约5.2MB） |
| celestial_expedition_v6.py | 模块化主程序 V6.3.1（需配合数据文件） |
| starfall_data_v6.py | 全量数据模块（职业/技能/装备/区域/BOSS等） |
| mods/ | 可选扩展：星尘纪元、星城、星辰龙、限定BOSS等 |
| 苍穹远征V6.3.1_单文件懒人包.zip | 懒人包：整合版+mods+说明 |

## 运行
```bash
python3 celestial_expedition_v631_singlefile.py
```
或解压懒人包后运行包内主程序。

## 特性
- 多档位存档：自定义档名、启动选档、双格式存档(.json/.gz)
- 星尘纪元扩展：新城/星城、星辰龙一族、冒险者公会
- 限定BOSS：终·星辉死神、最高作者
- 大世界：37区域、91 BOSS、9000+装备基底、17职业×400+技能
