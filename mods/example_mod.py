# -*- coding: utf-8 -*-
"""
星尘拓展包 v6.3 —— 星尘纪元（苍穹远征 V6.3 模组）
====================================================
适配苍穹远征 V6.3.0（celestial_expedition_v6.py，含启动入口修复版）。

本模组为最新版星尘模组：
  MOD_ID = "stardust"（主程序凭此登记 冒险者公会 / 限定BOSS）
仅当本模组加载时，主菜单才会开放：
  G 冒险者公会（悬赏榜 / 终·星辉死神挑战 / 声望商店）
  F 追更作者（主页追更按钮：点1次 → 作者变 1.8e+308 降神形态；
             再点1次 → 最弱形态 2000万血 + 无视护盾3000 + 一堆技能）
  H 挑战·最高作者（需先追更到最弱形态）
全新内容：
  - 新区域：新城 / 星城
  - 星辰龙一族：星辰龙幼体 / 星辰龙守卫 / 星辰龙[BOSS] /
                 万古星辰龙[BOSS] / 星海龙神[BOSS]
  - 全新装备/材料：星辰龙鳞、星辰龙冠、星系宝珠、死神残魂、作者签名卡等
  - 新事件若干
"""

MOD_NAME = "星尘拓展包"
MOD_ID = "stardust"
MOD_VERSION = "6.3.0"
MOD_DLC = True

MOD_ITEMS = {
    "mod_star_blade": {
        "name": "星尘之刃",
        "type": "weapon",
        "desc": "由模组添加的传说武器，剑身流转星尘。",
    },
    "mod_star_cloak": {
        "name": "星尘斗篷",
        "type": "armor",
        "desc": "由模组添加的护甲，抵御暗影侵蚀。",
    },
    "mod_star_ring": {
        "name": "星尘戒指",
        "type": "trinket",
        "desc": "由模组添加的饰品，蕴含星辰之力。",
    },
    "sd_dragon_scale": {
        "name": "星辰龙鳞",
        "type": "material",
        "desc": "从星辰龙身上剥落的鳞片，映着星河微光。",
    },
    "sd_dragon_crown": {
        "name": "星辰龙冠",
        "type": "accessory",
        "desc": "万古星辰龙以龙炎淬炼的冠冕，佩戴者受群星庇佑。",
    },
    "sd_galaxy_orb": {
        "name": "星系宝珠",
        "type": "accessory",
        "desc": "封印着一方小星系的宝珠，内部有银河缓缓旋转。",
    },
    "sd_reaper_soul": {
        "name": "死神残魂",
        "type": "trinket",
        "desc": "终·星辉死神陨落后逸散的星魂碎片，仍带着死亡的寒意。",
    },
    "sd_author_sig": {
        "name": "作者签名卡",
        "type": "trinket",
        "desc": "战胜最高作者后从他口袋搜出的签名卡，据说能让读者加更。",
    },
    "sd_stardust_elixir": {
        "name": "星尘圣水",
        "type": "material",
        "desc": "凝聚星尘的圣水，能抚平星辉级的创伤。",
    },
}

MOD_MONSTERS = [
    {
        "name": "星尘傀儡",
        "hp": 260,
        "atk": 22,
        "def": 10,
        "exp": 55,
        "gold": 40,
        "desc": "由模组添加的机械造物。",
    },
    {
        "name": "裂隙主宰",
        "hp": 900,
        "atk": 45,
        "def": 24,
        "exp": 220,
        "gold": 180,
        "boss": True,
        "desc": "由模组添加的 BOSS，镇守时空裂隙。",
    },
    {
        "name": "星海巡卫",
        "hp": 1200,
        "atk": 82,
        "def": 42,
        "exp": 210,
        "gold": 160,
        "desc": "新城上空巡弋的龙族卫兵，鳞片如星光闪烁。",
    },
    {
        "name": "星辰龙幼体",
        "hp": 1750,
        "atk": 98,
        "def": 50,
        "exp": 290,
        "gold": 220,
        "desc": "刚破壳的幼龙，吐息中带出点点星尘。",
    },
    {
        "name": "星辰龙守卫",
        "hp": 3200,
        "atk": 132,
        "def": 62,
        "exp": 520,
        "gold": 400,
        "desc": "镇守星城门户的成年龙族，龙威凛然。",
        "pierce": 60,
    },
    {
        "name": "星辰龙",
        "hp": 12800,
        "atk": 165,
        "def": 78,
        "exp": 2600,
        "gold": 1800,
        "boss": True,
        "desc": "星辰龙一族的主君，振翅便能掀起星河风暴。",
        "pierce": 200,
        "min_dmg": 120,
    },
    {
        "name": "万古星辰龙",
        "hp": 68000,
        "atk": 340,
        "def": 155,
        "exp": 13000,
        "gold": 9800,
        "boss": True,
        "desc": "活了万古的龙族始祖，鳞甲上铭刻着星河的兴衰。",
        "pierce": 520,
        "min_dmg": 300,
        "skills": [
            {"name": "星海吐息", "mult": 1.5},
            {"name": "万古龙威", "mult": 1.2, "flat": 300},
            {"name": "灭世龙焰", "mult": 2.0},
        ],
    },
    {
        "name": "星海龙神",
        "hp": 230000,
        "atk": 720,
        "def": 280,
        "exp": 65000,
        "gold": 46000,
        "boss": True,
        "desc": "化身星海的神龙，睁眼是白昼、闭眼是永夜。",
        "pierce": 900,
        "min_dmg": 600,
        "skills": [
            {"name": "银河龙息", "mult": 1.6},
            {"name": "星坠", "mult": 2.4},
            {"name": "龙神之怒", "mult": 1.4, "flat": 1200},
            {"name": "吞噬星辰", "mult": 3.0},
        ],
    },
]

# 新区域：monsters 为 MOD_MONSTERS 本地下标（0 起），主程序会自动映射全局下标
MOD_ZONES = [
    {
        "name": "新城",
        "level": 20,
        "desc": "龙与霓虹交织的现代都市：高塔刺破云层，龙影掠过灯海。",
        "monsters": [2, 3, 4, 5],
        "shop": ["mod_star_cloak", "mod_star_ring", "p2", "p3"],
        "final": False,
    },
    {
        "name": "星城",
        "level": 28,
        "desc": "悬浮于星河之上的龙族圣城，万古星辰龙与星海龙神在此沉眠。",
        "monsters": [3, 4, 5, 6, 7],
        "shop": ["sd_dragon_scale", "sd_galaxy_orb", "p3"],
        "final": False,
    },
]

MOD_EVENTS = [
    {
        "id": "mod_star_shower",
        "text": "星尘如雨般洒落，你沐浴其中，感到力量涌动。",
    },
    {
        "id": "mod_rift_call",
        "text": "一道时空裂隙在你面前展开，传来低沉的呼唤。",
    },
    {
        "id": "mod_dragon_roar",
        "text": "一声龙啸撕裂夜幕，新城上空的星尘云化作燃烧的轨迹。",
    },
    {
        "id": "mod_star_city_festival",
        "text": "星城正举行龙祭：鳞片在圣火中重铸，化作流光散入天际。",
    },
    {
        "id": "mod_author_rumor",
        "text": "旅人低声议论：那位「最高作者」据说常被读者追更追得满地图跑……",
    },
]

# V6.3 星尘纪元元数据：冒险者公会 / 限定BOSS（仅 MOD_ID=stardust 时由主程序登记）
STARDUST_META = {
    "name": "星尘纪元",
    "bounties": [
        {
            "target": "星辰龙",
            "name": "讨伐 星辰龙",
            "need": 1,
            "rep": 800,
            "gold": 4000,
            "item": "sd_dragon_scale",
        },
        {
            "target": "万古星辰龙",
            "name": "讨伐 万古星辰龙",
            "need": 1,
            "rep": 3000,
            "gold": 15000,
            "item": "sd_dragon_crown",
        },
        {
            "target": "星海龙神",
            "name": "讨伐 星海龙神",
            "need": 1,
            "rep": 9000,
            "gold": 50000,
            "item": "sd_galaxy_orb",
        },
        {
            "target": "终·星辉死神",
            "name": "讨伐 终·星辉死神",
            "need": 1,
            "rep": 22000,
            "gold": 120000,
            "item": "sd_reaper_soul",
        },
        {
            "target": "最高作者",
            "name": "终结 最高作者（最弱形态）",
            "need": 1,
            "rep": 60000,
            "gold": 500000,
            "item": "sd_author_sig",
        },
    ],
    "shop": [
        {"item": "mod_star_cloak", "price": 500, "name": "星尘斗篷"},
        {"item": "sd_dragon_scale", "price": 800, "name": "星辰龙鳞"},
        {"item": "sd_stardust_elixir", "price": 1200, "name": "星尘圣水"},
        {"item": "mod_star_ring", "price": 2000, "name": "星尘戒指"},
        {"item": "sd_dragon_crown", "price": 5000, "name": "星辰龙冠"},
        {"item": "sd_galaxy_orb", "price": 12000, "name": "星系宝珠"},
    ],
    "author_enabled": True,
    # 限定BOSS①：终·星辉死神（999万血 / 4500攻 / 保底伤害 / 无难度缩放）
    "death_spec": {
        "name": "终·星辉死神",
        "hp": 9990000,
        "atk": 4500,
        "def": 350,
        "exp": 600000,
        "gold": 300000,
        "boss": True,
        "desc": "收割过万千星辰的死神，镰刃所指即是终焉。",
        "pierce": 500,
        "min_dmg": 800,
        "skills": [
            {"name": "死星·终焉", "mult": 1.6},
            {"name": "镰刃·灭世", "mult": 2.0},
            {"name": "魂归星海", "flat": 2500},
            {"name": "死神凝视", "mult": 1.2, "flat": 1500},
        ],
    },
    # 限定BOSS②：最高作者（主页 F 追更触发）
    # phase0 = 真身(∞/∞，展示用，主程序禁止挑战)
    # phase1 = 降神形态(1.8e+308，主程序禁止挑战)
    # phase2 = 最弱形态(2000万血 / 无视护盾3000 / 一堆技能，可挑战)
    "author_phases": [
        {
            "name": "最高作者",
            "hp": 1e308,
            "atk": 1e308,
            "def": 999999999999,
            "exp": 0,
            "gold": 0,
            "boss": True,
            "desc": "真身形态：不可挑战。",
        },
        {
            "name": "最高作者",
            "hp": 1.8e308,
            "atk": 1.8e308,
            "def": 999999999,
            "exp": 0,
            "gold": 0,
            "boss": True,
            "desc": "降神形态：血攻 1.8e+308，仍在神域。",
        },
        {
            "name": "最高作者",
            "hp": 20000000,
            "atk": 9000,
            "def": 15000,
            "exp": 99999999,
            "gold": 9999999,
            "boss": True,
            "desc": "被读者追更追到脱力的最弱形态。",
            "pierce": 3000,
            "min_dmg": 3000,
            "skills": [
                {"name": "作者の狂暴", "mult": 2.2},
                {"name": "删评警告", "flat": 6000},
                {"name": "断更神罚", "mult": 1.5, "flat": 2000},
                {"name": "读者の怨念", "flat": 9999},
                {"name": "键盘の制裁", "mult": 1.2, "flat": 3000},
            ],
        },
    ],
}
