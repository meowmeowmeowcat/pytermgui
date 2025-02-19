SVG_TARGET = """\
<svg width="939.0" height="706.25" viewBox="0 0 939.0 706.25"
     xmlns="http://www.w3.org/2000/svg">
    <style>
        body {
            --ptg-background: #000000;
            --ptg-foreground: #ffffff;
            color: var(--ptg-foreground);
            margin: 70px;
        }
        span {
            display: inline-block;
        }
        code {
            font-family: Menlo, 'DejaVu Sans Mono', consolas, 'Courier New', monospace;
            line-height: 1.2em;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
        #ptg-terminal {
            position: relative;
            display: flex;
            flex-direction: column;
            background-color: var(--ptg-background);
            border-radius: 9px;
            box-shadow: 0 22px 70px 4px rgba(0, 0, 0, 0.56);
            width: 769.0px;
            height: 536.25px;
        }
        #ptg-terminal-navbuttons {
            position: absolute;
            top: 8px;
            left: 8px;
        }
        #ptg-terminal-body {
            margin: 15px;
            font-size: 15px;
            overflow: hidden scroll;
            white-space: normal;
        }
        #ptg-terminal-title {
            font-family: sans-serif;
            font-size: 12px;
            font-weight: bold;
            color: #95989b;
            margin-top: 4px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .ptg-position {
            position: absolute;
        }

.ptg0 {background-color: var(--ptg-background); color:#ffd787; background-color:#afaf00}
.ptg1 {background-color: var(--ptg-background); color:#5fff00; background-color:#875f87}
.ptg2 {background-color: var(--ptg-background); color:#afaf5f; background-color:#af87af}
.ptg3 {background-color: var(--ptg-background); color:#ff00af; background-color:#0087d7}
.ptg4 {background-color: var(--ptg-background); color:#ffd75f; background-color:#d7af5f}
.ptg5 {background-color: var(--ptg-background); color:#5faf00; background-color:#d7ff5f}
.ptg6 {background-color: var(--ptg-background); color:#5f005f; background-color:#ffaf00}
.ptg7 {background-color: var(--ptg-background); color:#00ffaf; background-color:#af00af}
.ptg8 {background-color: var(--ptg-background); color:#87ffd7; background-color:#ff87af}
.ptg9 {background-color: var(--ptg-background); color:#00af5f; background-color:#005faf}
.ptg10 {background-color: var(--ptg-background); color:#5f87ff; background-color:#8700ff}
.ptg11 {background-color: var(--ptg-background); color:#d70087; background-color:#5f5faf}
.ptg12 {background-color: var(--ptg-background); color:#d75f5f; background-color:#5f5f87}
.ptg13 {background-color: var(--ptg-background); color:#afafd7; background-color:#8787af}
.ptg14 {background-color: var(--ptg-background); color:#87d787; background-color:#87afaf}
.ptg15 {background-color: var(--ptg-background); color:#ff87ff; background-color:#afd787}
.ptg16 {background-color: var(--ptg-background); color:#d7d75f; background-color:#00af87}
.ptg17 {background-color: var(--ptg-background); color:#d75f5f; background-color:#d700ff}
.ptg18 {background-color: var(--ptg-background); color:#87ff00; background-color:#d7d7d7}
.ptg19 {background-color: var(--ptg-background); color:#5f5fd7; background-color:#8787af}
.ptg20 {background-color: var(--ptg-background); color:#ff0000; background-color:#5f00af}
.ptg21 {background-color: var(--ptg-background); color:#d75fd7; background-color:#d75f5f}
.ptg22 {background-color: var(--ptg-background); color:#00afd7; background-color:#ff87d7}
.ptg23 {background-color: var(--ptg-background); color:#ff5f87; background-color:#5f0000}
.ptg24 {background-color: var(--ptg-background); color:#8700d7; background-color:#afd7af}
.ptg25 {background-color: var(--ptg-background); color:#00ff5f; background-color:#87d787}
.ptg26 {background-color: var(--ptg-background); color:#ffafaf; background-color:#ff87ff}
.ptg27 {background-color: var(--ptg-background); color:#0000ff; background-color:#5f875f}
.ptg28 {background-color: var(--ptg-background); color:#00ffff; background-color:#5f5f00}
.ptg29 {background-color: var(--ptg-background); color:#d75f5f; background-color:#87875f}
.ptg30 {background-color: var(--ptg-background); color:#d78787; background-color:#d7af00}
.ptg31 {background-color: var(--ptg-background); color:#ff0000; background-color:#5fff5f}
.ptg32 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#d75f87}
.ptg33 {background-color: var(--ptg-background); color:#afd700; background-color:#ff87af}
.ptg34 {background-color: var(--ptg-background); color:#af5f00; background-color:#000087}
.ptg35 {background-color: var(--ptg-background); color:#af0087; background-color:#875f5f}
.ptg36 {background-color: var(--ptg-background); color:#005fff; background-color:#ffd787}
.ptg37 {background-color: var(--ptg-background); color:#00ffff; background-color:#5f0000}
.ptg38 {background-color: var(--ptg-background); color:#d7af87; background-color:#ff5faf}
.ptg39 {background-color: var(--ptg-background); color:#00ff5f; background-color:#d78700}
.ptg40 {background-color: var(--ptg-background); color:#afaf00; background-color:#5fff00}
.ptg41 {background-color: var(--ptg-background); color:#5f0087; background-color:#afafff}
.ptg42 {background-color: var(--ptg-background); color:#8787d7; background-color:#d7afaf}
.ptg43 {background-color: var(--ptg-background); color:#5f5fff; background-color:#d70087}
.ptg44 {background-color: var(--ptg-background); color:#0000ff; background-color:#87005f}
.ptg45 {background-color: var(--ptg-background); color:#5fffff; background-color:#ffff00}
.ptg46 {background-color: var(--ptg-background); color:#87d75f; background-color:#af8700}
.ptg47 {background-color: var(--ptg-background); color:#d7d787; background-color:#8700d7}
.ptg48 {background-color: var(--ptg-background); color:#afafd7; background-color:#008787}
.ptg49 {background-color: var(--ptg-background); color:#ff87d7; background-color:#5fff87}
.ptg50 {background-color: var(--ptg-background); color:#5f87ff; background-color:#5f8787}
.ptg51 {background-color: var(--ptg-background); color:#af5fd7; background-color:#d7afff}
.ptg52 {background-color: var(--ptg-background); color:#afffaf; background-color:#ffffaf}
.ptg53 {background-color: var(--ptg-background); color:#87d7d7; background-color:#878700}
.ptg54 {background-color: var(--ptg-background); color:#ffff00; background-color:#d70000}
.ptg55 {background-color: var(--ptg-background); color:#5f5fff; background-color:#5fff00}
.ptg56 {background-color: var(--ptg-background); color:#ff0087; background-color:#ffafd7}
.ptg57 {background-color: var(--ptg-background); color:#ffffff; background-color:#ffd7af}
.ptg58 {background-color: var(--ptg-background); color:#ffafff; background-color:#0087d7}
.ptg59 {background-color: var(--ptg-background); color:#ff00af; background-color:#afd7ff}
.ptg60 {background-color: var(--ptg-background); color:#00ff5f; background-color:#d7af00}
.ptg61 {background-color: var(--ptg-background); color:#00d7d7; background-color:#5f875f}
.ptg62 {background-color: var(--ptg-background); color:#000087; background-color:#00afff}
.ptg63 {background-color: var(--ptg-background); color:#00d7ff; background-color:#d7d7d7}
.ptg64 {background-color: var(--ptg-background); color:#d7d7d7; background-color:#ffff00}
.ptg65 {background-color: var(--ptg-background); color:#00ffaf; background-color:#5fafff}
.ptg66 {background-color: var(--ptg-background); color:#0087ff; background-color:#afffff}
.ptg67 {background-color: var(--ptg-background); color:#5f0000; background-color:#00d787}
.ptg68 {background-color: var(--ptg-background); color:#87ffff; background-color:#afaf5f}
.ptg69 {background-color: var(--ptg-background); color:#ff87af; background-color:#afff00}
.ptg70 {background-color: var(--ptg-background); color:#5fff87; background-color:#ffff87}
.ptg71 {background-color: var(--ptg-background); color:#ff8787; background-color:#d7af5f}
.ptg72 {background-color: var(--ptg-background); color:#afffff; background-color:#8787d7}
.ptg73 {background-color: var(--ptg-background); color:#d7ffff; background-color:#5fffaf}
.ptg74 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#af00d7}
.ptg75 {background-color: var(--ptg-background); color:#d78787; background-color:#00ff87}
.ptg76 {background-color: var(--ptg-background); color:#ff5fd7; background-color:#d7ffff}
.ptg77 {background-color: var(--ptg-background); color:#ffafff; background-color:#d7afff}
.ptg78 {background-color: var(--ptg-background); color:#ff8700; background-color:#00d7af}
.ptg79 {background-color: var(--ptg-background); color:#00005f; background-color:#005f00}
.ptg80 {background-color: var(--ptg-background); color:#ffd75f; background-color:#d7ff5f}
.ptg81 {background-color: var(--ptg-background); color:#d75f5f; background-color:#5f00af}
.ptg82 {background-color: var(--ptg-background); color:#875f00; background-color:#d7ff00}
.ptg83 {background-color: var(--ptg-background); color:#afffff; background-color:#5fffd7}
.ptg84 {background-color: var(--ptg-background); color:#0000ff; background-color:#0087af}
.ptg85 {background-color: var(--ptg-background); color:#d787af; background-color:#af87af}
.ptg86 {background-color: var(--ptg-background); color:#ffff00; background-color:#ffff87}
.ptg87 {background-color: var(--ptg-background); color:#afd75f; background-color:#5f00af}
.ptg88 {background-color: var(--ptg-background); color:#d70000; background-color:#87d7ff}
.ptg89 {background-color: var(--ptg-background); color:#d7af5f; background-color:#d7afd7}
.ptg90 {background-color: var(--ptg-background); color:#000087; background-color:#87afd7}
.ptg91 {background-color: var(--ptg-background); color:#ffd75f; background-color:#5f005f}
.ptg92 {background-color: var(--ptg-background); color:#5fffaf; background-color:#87ff87}
.ptg93 {background-color: var(--ptg-background); color:#5f00af; background-color:#af87af}
.ptg94 {background-color: var(--ptg-background); color:#af0087; background-color:#af00ff}
.ptg95 {background-color: var(--ptg-background); color:#ff8787; background-color:#87ffd7}
.ptg96 {background-color: var(--ptg-background); color:#005f5f; background-color:#d7d7ff}
.ptg97 {background-color: var(--ptg-background); color:#afaf00; background-color:#5faf87}
.ptg98 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#ff5faf}
.ptg99 {background-color: var(--ptg-background); color:#ffff87; background-color:#afd787}
.ptg100 {background-color: var(--ptg-background); color:#00ffaf; background-color:#afd75f}
.ptg101 {background-color: var(--ptg-background); color:#af00d7; background-color:#ff00af}
.ptg102 {background-color: var(--ptg-background); color:#5f00ff; background-color:#00d7d7}
.ptg103 {background-color: var(--ptg-background); color:#5fd7ff; background-color:#5f5f87}
.ptg104 {background-color: var(--ptg-background); color:#5fd7af; background-color:#5fffaf}
.ptg105 {background-color: var(--ptg-background); color:#87ff87; background-color:#0087ff}
.ptg106 {background-color: var(--ptg-background); color:#ffffff; background-color:#afafaf}
.ptg107 {background-color: var(--ptg-background); color:#87d700; background-color:#ff5fff}
.ptg108 {background-color: var(--ptg-background); color:#00afaf; background-color:#00afaf}
.ptg109 {background-color: var(--ptg-background); color:#87ffff; background-color:#870000}
.ptg110 {background-color: var(--ptg-background); color:#ffafd7; background-color:#5f005f}
.ptg111 {background-color: var(--ptg-background); color:#005f5f; background-color:#5faf00}
.ptg112 {background-color: var(--ptg-background); color:#af8787; background-color:#af87af}
.ptg113 {background-color: var(--ptg-background); color:#d75faf; background-color:#87d7af}
.ptg114 {background-color: var(--ptg-background); color:#87005f; background-color:#ff8700}
.ptg115 {background-color: var(--ptg-background); color:#5fffd7; background-color:#d7d75f}
.ptg116 {background-color: var(--ptg-background); color:#00af5f; background-color:#5fd7d7}
.ptg117 {background-color: var(--ptg-background); color:#d7ffaf; background-color:#d7005f}
.ptg118 {background-color: var(--ptg-background); color:#d7d700; background-color:#afaf00}
.ptg119 {background-color: var(--ptg-background); color:#af0087; background-color:#00d7ff}
.ptg120 {background-color: var(--ptg-background); color:#8700ff; background-color:#ff0087}
.ptg121 {background-color: var(--ptg-background); color:#5fff87; background-color:#afff00}
.ptg122 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#afffaf}
.ptg123 {background-color: var(--ptg-background); color:#87d7af; background-color:#af00ff}
.ptg124 {background-color: var(--ptg-background); color:#005f87; background-color:#ff00af}
.ptg125 {background-color: var(--ptg-background); color:#00ffaf; background-color:#5faf5f}
.ptg126 {background-color: var(--ptg-background); color:#af5f87; background-color:#87afaf}
.ptg127 {background-color: var(--ptg-background); color:#afffaf; background-color:#ffafaf}
.ptg128 {background-color: var(--ptg-background); color:#afd7af; background-color:#d7d787}
.ptg129 {background-color: var(--ptg-background); color:#afafaf; background-color:#8700af}
.ptg130 {background-color: var(--ptg-background); color:#afff00; background-color:#87af5f}
.ptg131 {background-color: var(--ptg-background); color:#5fafd7; background-color:#af005f}
.ptg132 {background-color: var(--ptg-background); color:#00d75f; background-color:#00af87}
.ptg133 {background-color: var(--ptg-background); color:#ffafd7; background-color:#afff87}
.ptg134 {background-color: var(--ptg-background); color:#5fff00; background-color:#ffafd7}
.ptg135 {background-color: var(--ptg-background); color:#d7af5f; background-color:#008787}
.ptg136 {background-color: var(--ptg-background); color:#005f87; background-color:#ffaf87}
.ptg137 {background-color: var(--ptg-background); color:#d7d787; background-color:#ffafd7}
.ptg138 {background-color: var(--ptg-background); color:#00d7ff; background-color:#87af00}
.ptg139 {background-color: var(--ptg-background); color:#875faf; background-color:#af00af}
.ptg140 {background-color: var(--ptg-background); color:#87afff; background-color:#d787af}
.ptg141 {background-color: var(--ptg-background); color:#ff8787; background-color:#875f5f}
.ptg142 {background-color: var(--ptg-background); color:#878700; background-color:#5f5faf}
.ptg143 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#d78787}
.ptg144 {background-color: var(--ptg-background); color:#87ff5f; background-color:#af0000}
.ptg145 {background-color: var(--ptg-background); color:#d7ffaf; background-color:#ff00d7}
.ptg146 {background-color: var(--ptg-background); color:#ffaf00; background-color:#5f0000}
.ptg147 {background-color: var(--ptg-background); color:#5f005f; background-color:#5faf87}
.ptg148 {background-color: var(--ptg-background); color:#005fff; background-color:#00ffaf}
.ptg149 {background-color: var(--ptg-background); color:#5f0087; background-color:#00875f}
.ptg150 {background-color: var(--ptg-background); color:#d70087; background-color:#000087}
.ptg151 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#d7af00}
.ptg152 {background-color: var(--ptg-background); color:#87d7d7; background-color:#d75fff}
.ptg153 {background-color: var(--ptg-background); color:#87d7af; background-color:#ffff87}
.ptg154 {background-color: var(--ptg-background); color:#ff87af; background-color:#d75f87}
.ptg155 {background-color: var(--ptg-background); color:#87875f; background-color:#afffaf}
.ptg156 {background-color: var(--ptg-background); color:#5fd787; background-color:#af5f5f}
.ptg157 {background-color: var(--ptg-background); color:#87afff; background-color:#afd787}
.ptg158 {background-color: var(--ptg-background); color:#00ffd7; background-color:#5faf5f}
.ptg159 {background-color: var(--ptg-background); color:#d75faf; background-color:#ffd787}
.ptg160 {background-color: var(--ptg-background); color:#5fffaf; background-color:#870000}
.ptg161 {background-color: var(--ptg-background); color:#00ffd7; background-color:#ffd700}
.ptg162 {background-color: var(--ptg-background); color:#ffaf87; background-color:#87ff5f}
.ptg163 {background-color: var(--ptg-background); color:#5fd787; background-color:#d7d7af}
.ptg164 {background-color: var(--ptg-background); color:#d7afff; background-color:#d70000}
.ptg165 {background-color: var(--ptg-background); color:#0087ff; background-color:#afd7af}
.ptg166 {background-color: var(--ptg-background); color:#ffd700; background-color:#87ff5f}
.ptg167 {background-color: var(--ptg-background); color:#afd7ff; background-color:#875f00}
.ptg168 {background-color: var(--ptg-background); color:#ffff87; background-color:#87ffaf}
.ptg169 {background-color: var(--ptg-background); color:#00afff; background-color:#ff5f87}
.ptg170 {background-color: var(--ptg-background); color:#af5f5f; background-color:#5f8787}
.ptg171 {background-color: var(--ptg-background); color:#5fd7ff; background-color:#870000}
.ptg172 {background-color: var(--ptg-background); color:#875fff; background-color:#5fafaf}
.ptg173 {background-color: var(--ptg-background); color:#ffd7af; background-color:#87d7af}
.ptg174 {background-color: var(--ptg-background); color:#ffff5f; background-color:#878787}
.ptg175 {background-color: var(--ptg-background); color:#d7af00; background-color:#87d7af}
.ptg176 {background-color: var(--ptg-background); color:#5f0087; background-color:#d7ff00}
.ptg177 {background-color: var(--ptg-background); color:#5f0000; background-color:#ff00d7}
.ptg178 {background-color: var(--ptg-background); color:#00afd7; background-color:#5f0000}
.ptg179 {background-color: var(--ptg-background); color:#ff875f; background-color:#5fafff}
.ptg180 {background-color: var(--ptg-background); color:#8787ff; background-color:#af00af}
.ptg181 {background-color: var(--ptg-background); color:#87af5f; background-color:#00d787}
.ptg182 {background-color: var(--ptg-background); color:#5fffd7; background-color:#af0000}
.ptg183 {background-color: var(--ptg-background); color:#af5f5f; background-color:#87af00}
.ptg184 {background-color: var(--ptg-background); color:#af87d7; background-color:#afaf00}
.ptg185 {background-color: var(--ptg-background); color:#af00af; background-color:#d7ff00}
.ptg186 {background-color: var(--ptg-background); color:#5f8700; background-color:#005f00}
.ptg187 {background-color: var(--ptg-background); color:#005f87; background-color:#080808}
.ptg188 {background-color: var(--ptg-background); color:#ffffd7; background-color:#87005f}
.ptg189 {background-color: var(--ptg-background); color:#0000af; background-color:#ffafaf}
.ptg190 {background-color: var(--ptg-background); color:#878700; background-color:#d7ff87}
.ptg191 {background-color: var(--ptg-background); color:#87af5f; background-color:#ff87ff}
.ptg192 {background-color: var(--ptg-background); color:#87d700; background-color:#87005f}
.ptg193 {background-color: var(--ptg-background); color:#ff5fff; background-color:#875f87}
.ptg194 {background-color: var(--ptg-background); color:#ffaf00; background-color:#5f005f}
.ptg195 {background-color: var(--ptg-background); color:#af0000; background-color:#87d75f}
.ptg196 {background-color: var(--ptg-background); color:#af00d7; background-color:#d75f87}
.ptg197 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#87ff5f}
.ptg198 {background-color: var(--ptg-background); color:#ff5f00; background-color:#87ff00}
.ptg199 {background-color: var(--ptg-background); color:#af5f5f; background-color:#5f5f5f}
.ptg200 {background-color: var(--ptg-background); color:#d7af87; background-color:#5fff5f}
.ptg201 {background-color: var(--ptg-background); color:#005faf; background-color:#d7d700}
.ptg202 {background-color: var(--ptg-background); color:#ff875f; background-color:#5fd75f}
.ptg203 {background-color: var(--ptg-background); color:#ff5fff; background-color:#87d700}
.ptg204 {background-color: var(--ptg-background); color:#87afd7; background-color:#5f5f87}
.ptg205 {background-color: var(--ptg-background); color:#af5f00; background-color:#d7af5f}
.ptg206 {background-color: var(--ptg-background); color:#5f87d7; background-color:#d7ffaf}
.ptg207 {background-color: var(--ptg-background); color:#0000af; background-color:#d75fd7}
.ptg208 {background-color: var(--ptg-background); color:#ffffff; background-color:#afafd7}
.ptg209 {background-color: var(--ptg-background); color:#af00d7; background-color:#afd700}
.ptg210 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#875f5f}
.ptg211 {background-color: var(--ptg-background); color:#af005f; background-color:#5fafff}
.ptg212 {background-color: var(--ptg-background); color:#d7d7ff; background-color:#5fff5f}
.ptg213 {background-color: var(--ptg-background); color:#ffff00; background-color:#d7af5f}
.ptg214 {background-color: var(--ptg-background); color:#008787; background-color:#d7d7af}
.ptg215 {background-color: var(--ptg-background); color:#5fd7ff; background-color:#875f00}
.ptg216 {background-color: var(--ptg-background); color:#ff0087; background-color:#5fafaf}
.ptg217 {background-color: var(--ptg-background); color:#080808; background-color:#ff00d7}
.ptg218 {background-color: var(--ptg-background); color:#00005f; background-color:#d7ffd7}
.ptg219 {background-color: var(--ptg-background); color:#00af5f; background-color:#ffd7d7}
.ptg220 {background-color: var(--ptg-background); color:#00afaf; background-color:#d7ffff}
.ptg221 {background-color: var(--ptg-background); color:#d7af87; background-color:#ffff00}
.ptg222 {background-color: var(--ptg-background); color:#87d7d7; background-color:#5f5faf}
.ptg223 {background-color: var(--ptg-background); color:#d70000; background-color:#d75f87}
.ptg224 {background-color: var(--ptg-background); color:#87d75f; background-color:#af00d7}
.ptg225 {background-color: var(--ptg-background); color:#d787af; background-color:#5f875f}
.ptg226 {background-color: var(--ptg-background); color:#00875f; background-color:#87ffff}
.ptg227 {background-color: var(--ptg-background); color:#5fd700; background-color:#8700d7}
.ptg228 {background-color: var(--ptg-background); color:#0087ff; background-color:#d7afff}
.ptg229 {background-color: var(--ptg-background); color:#00ff00; background-color:#d70000}
.ptg230 {background-color: var(--ptg-background); color:#d787af; background-color:#00afff}
.ptg231 {background-color: var(--ptg-background); color:#005fd7; background-color:#ffff5f}
.ptg232 {background-color: var(--ptg-background); color:#d7af00; background-color:#5faf00}
.ptg233 {background-color: var(--ptg-background); color:#00ff87; background-color:#00afaf}
.ptg234 {background-color: var(--ptg-background); color:#5f8787; background-color:#afffd7}
.ptg235 {background-color: var(--ptg-background); color:#5f8700; background-color:#ffd75f}
.ptg236 {background-color: var(--ptg-background); color:#008787; background-color:#afd7d7}
.ptg237 {background-color: var(--ptg-background); color:#ff87af; background-color:#870087}
.ptg238 {background-color: var(--ptg-background); color:#87ffff; background-color:#d787ff}
.ptg239 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#ffd7d7}
.ptg240 {background-color: var(--ptg-background); color:#d7d7ff; background-color:#ff5faf}
.ptg241 {background-color: var(--ptg-background); color:#d700ff; background-color:#d7af00}
.ptg242 {background-color: var(--ptg-background); color:#ffd7d7; background-color:#af00af}
.ptg243 {background-color: var(--ptg-background); color:#d7af87; background-color:#87ffff}
.ptg244 {background-color: var(--ptg-background); color:#af5faf; background-color:#87d700}
.ptg245 {background-color: var(--ptg-background); color:#00d7af; background-color:#ff875f}
.ptg246 {background-color: var(--ptg-background); color:#ff5f87; background-color:#af87ff}
.ptg247 {background-color: var(--ptg-background); color:#5fff5f; background-color:#0000af}
.ptg248 {background-color: var(--ptg-background); color:#5fd787; background-color:#875f00}
.ptg249 {background-color: var(--ptg-background); color:#5fff87; background-color:#ffafd7}
.ptg250 {background-color: var(--ptg-background); color:#875fff; background-color:#d75fd7}
.ptg251 {background-color: var(--ptg-background); color:#000087; background-color:#5faf5f}
.ptg252 {background-color: var(--ptg-background); color:#ff87d7; background-color:#d75f5f}
.ptg253 {background-color: var(--ptg-background); color:#afaf87; background-color:#5f5f5f}
.ptg254 {background-color: var(--ptg-background); color:#87ff87; background-color:#af5f5f}
.ptg255 {background-color: var(--ptg-background); color:#af5f00; background-color:#d7ff5f}
.ptg256 {background-color: var(--ptg-background); color:#87d700; background-color:#afafff}
.ptg257 {background-color: var(--ptg-background); color:#00ff5f; background-color:#5f0000}
.ptg258 {background-color: var(--ptg-background); color:#8787af; background-color:#005f00}
.ptg259 {background-color: var(--ptg-background); color:#8787af; background-color:#d7ffd7}
.ptg260 {background-color: var(--ptg-background); color:#875faf; background-color:#afd787}
.ptg261 {background-color: var(--ptg-background); color:#00ffd7; background-color:#005fd7}
.ptg262 {background-color: var(--ptg-background); color:#afaf5f; background-color:#875f5f}
.ptg263 {background-color: var(--ptg-background); color:#87afd7; background-color:#00af00}
.ptg264 {background-color: var(--ptg-background); color:#875f87; background-color:#ff87d7}
.ptg265 {background-color: var(--ptg-background); color:#5faf87; background-color:#878787}
.ptg266 {background-color: var(--ptg-background); color:#5fff5f; background-color:#87ffaf}
.ptg267 {background-color: var(--ptg-background); color:#af5f00; background-color:#5f8787}
.ptg268 {background-color: var(--ptg-background); color:#87afff; background-color:#af5f87}
.ptg269 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#00875f}
.ptg270 {background-color: var(--ptg-background); color:#5fd75f; background-color:#d7af87}
.ptg271 {background-color: var(--ptg-background); color:#d70087; background-color:#875f87}
.ptg272 {background-color: var(--ptg-background); color:#8700d7; background-color:#5f5fff}
.ptg273 {background-color: var(--ptg-background); color:#5f875f; background-color:#8700af}
.ptg274 {background-color: var(--ptg-background); color:#d7d787; background-color:#ffffaf}
.ptg275 {background-color: var(--ptg-background); color:#5f87d7; background-color:#8787d7}
.ptg276 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#00005f}
.ptg277 {background-color: var(--ptg-background); color:#d7d700; background-color:#d7ffff}
.ptg278 {background-color: var(--ptg-background); color:#afafaf; background-color:#ff87ff}
.ptg279 {background-color: var(--ptg-background); color:#ffafaf; background-color:#000087}
.ptg280 {background-color: var(--ptg-background); color:#af0087; background-color:#5fafd7}
.ptg281 {background-color: var(--ptg-background); color:#8787af; background-color:#d7d7d7}
.ptg282 {background-color: var(--ptg-background); color:#87afd7; background-color:#5fafd7}
.ptg283 {background-color: var(--ptg-background); color:#005f87; background-color:#5f87ff}
.ptg284 {background-color: var(--ptg-background); color:#005faf; background-color:#ff8787}
.ptg285 {background-color: var(--ptg-background); color:#00ff87; background-color:#ff5f87}
.ptg286 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#d7afff}
.ptg287 {background-color: var(--ptg-background); color:#5fafd7; background-color:#d75f00}
.ptg288 {background-color: var(--ptg-background); color:#ff87d7; background-color:#5faf5f}
.ptg289 {background-color: var(--ptg-background); color:#870000; background-color:#00d75f}
.ptg290 {background-color: var(--ptg-background); color:#afd787; background-color:#afffff}
.ptg291 {background-color: var(--ptg-background); color:#d7d787; background-color:#080808}
.ptg292 {background-color: var(--ptg-background); color:#00d75f; background-color:#af87ff}
.ptg293 {background-color: var(--ptg-background); color:#00ff87; background-color:#00d7ff}
.ptg294 {background-color: var(--ptg-background); color:#005f87; background-color:#af5fff}
.ptg295 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#d7005f}
.ptg296 {background-color: var(--ptg-background); color:#ffafaf; background-color:#ff005f}
.ptg297 {background-color: var(--ptg-background); color:#875f87; background-color:#878700}
.ptg298 {background-color: var(--ptg-background); color:#5f5faf; background-color:#ffff87}
.ptg299 {background-color: var(--ptg-background); color:#0000d7; background-color:#d75fd7}
.ptg300 {background-color: var(--ptg-background); color:#af87ff; background-color:#87ff5f}
.ptg301 {background-color: var(--ptg-background); color:#afaf00; background-color:#afd7af}
.ptg302 {background-color: var(--ptg-background); color:#ffff87; background-color:#5fd7d7}
.ptg303 {background-color: var(--ptg-background); color:#d75faf; background-color:#afffaf}
.ptg304 {background-color: var(--ptg-background); color:#00afff; background-color:#5fd75f}
.ptg305 {background-color: var(--ptg-background); color:#afd7af; background-color:#af00ff}
.ptg306 {background-color: var(--ptg-background); color:#0000ff; background-color:#d7afff}
.ptg307 {background-color: var(--ptg-background); color:#87d7ff; background-color:#00d7af}
.ptg308 {background-color: var(--ptg-background); color:#00d787; background-color:#d70087}
.ptg309 {background-color: var(--ptg-background); color:#00d787; background-color:#d75f5f}
.ptg310 {background-color: var(--ptg-background); color:#87afd7; background-color:#ffff00}
.ptg311 {background-color: var(--ptg-background); color:#d787af; background-color:#5f87af}
.ptg312 {background-color: var(--ptg-background); color:#ff5f00; background-color:#5fd75f}
.ptg313 {background-color: var(--ptg-background); color:#080808; background-color:#87d7ff}
.ptg314 {background-color: var(--ptg-background); color:#ff8787; background-color:#af5f87}
.ptg315 {background-color: var(--ptg-background); color:#af00ff; background-color:#875faf}
.ptg316 {background-color: var(--ptg-background); color:#5f00ff; background-color:#afd787}
.ptg317 {background-color: var(--ptg-background); color:#870000; background-color:#5fff87}
.ptg318 {background-color: var(--ptg-background); color:#ffff5f; background-color:#00d7ff}
.ptg319 {background-color: var(--ptg-background); color:#5f00af; background-color:#5f8787}
.ptg320 {background-color: var(--ptg-background); color:#5fd700; background-color:#ffd787}
.ptg321 {background-color: var(--ptg-background); color:#00af5f; background-color:#00ff5f}
.ptg322 {background-color: var(--ptg-background); color:#ffd7af; background-color:#ff87ff}
.ptg323 {background-color: var(--ptg-background); color:#87afff; background-color:#87d7ff}
.ptg324 {background-color: var(--ptg-background); color:#875f87; background-color:#ff0087}
.ptg325 {background-color: var(--ptg-background); color:#5fff00; background-color:#87ff5f}
.ptg326 {background-color: var(--ptg-background); color:#00ff5f; background-color:#d7afaf}
.ptg327 {background-color: var(--ptg-background); color:#ffd7d7; background-color:#5faf87}
.ptg328 {background-color: var(--ptg-background); color:#5fafaf; background-color:#d7ff00}
.ptg329 {background-color: var(--ptg-background); color:#87d75f; background-color:#af5fd7}
.ptg330 {background-color: var(--ptg-background); color:#87d7ff; background-color:#af5faf}
.ptg331 {background-color: var(--ptg-background); color:#af87ff; background-color:#d7ffaf}
.ptg332 {background-color: var(--ptg-background); color:#005f00; background-color:#ffd700}
.ptg333 {background-color: var(--ptg-background); color:#ffd700; background-color:#d78787}
.ptg334 {background-color: var(--ptg-background); color:#af5fff; background-color:#afffaf}
.ptg335 {background-color: var(--ptg-background); color:#5fff5f; background-color:#ff00d7}
.ptg336 {background-color: var(--ptg-background); color:#d7d75f; background-color:#00ff87}
.ptg337 {background-color: var(--ptg-background); color:#ff8787; background-color:#ffffff}
.ptg338 {background-color: var(--ptg-background); color:#005fd7; background-color:#afffaf}
.ptg339 {background-color: var(--ptg-background); color:#5fafd7; background-color:#ffff00}
.ptg340 {background-color: var(--ptg-background); color:#5f87af; background-color:#afff5f}
.ptg341 {background-color: var(--ptg-background); color:#ffff5f; background-color:#af00d7}
.ptg342 {background-color: var(--ptg-background); color:#af87af; background-color:#afaf87}
.ptg343 {background-color: var(--ptg-background); color:#080808; background-color:#00d7d7}
.ptg344 {background-color: var(--ptg-background); color:#870087; background-color:#5fafaf}
.ptg345 {background-color: var(--ptg-background); color:#d7ff87; background-color:#5fd7af}
.ptg346 {background-color: var(--ptg-background); color:#ffd7af; background-color:#ff87af}
.ptg347 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#afaf87}
.ptg348 {background-color: var(--ptg-background); color:#afaf00; background-color:#00875f}
.ptg349 {background-color: var(--ptg-background); color:#87d7ff; background-color:#00d7d7}
.ptg350 {background-color: var(--ptg-background); color:#ff875f; background-color:#00d7ff}
.ptg351 {background-color: var(--ptg-background); color:#d7d700; background-color:#d7af00}
.ptg352 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#ff87ff}
.ptg353 {background-color: var(--ptg-background); color:#ffafff; background-color:#87ffd7}
.ptg354 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#875f87}
.ptg355 {background-color: var(--ptg-background); color:#afafaf; background-color:#ffffd7}
.ptg356 {background-color: var(--ptg-background); color:#ffaf00; background-color:#870087}
.ptg357 {background-color: var(--ptg-background); color:#af5fd7; background-color:#87875f}
.ptg358 {background-color: var(--ptg-background); color:#d7ff87; background-color:#ffaf87}
.ptg359 {background-color: var(--ptg-background); color:#5fafaf; background-color:#5fd7ff}
.ptg360 {background-color: var(--ptg-background); color:#00afff; background-color:#ff87d7}
.ptg361 {background-color: var(--ptg-background); color:#d75faf; background-color:#00005f}
.ptg362 {background-color: var(--ptg-background); color:#af0087; background-color:#d7ffd7}
.ptg363 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#875f5f}
.ptg364 {background-color: var(--ptg-background); color:#0000af; background-color:#af875f}
.ptg365 {background-color: var(--ptg-background); color:#d7ff5f; background-color:#5fffd7}
.ptg366 {background-color: var(--ptg-background); color:#d7d700; background-color:#ff5fff}
.ptg367 {background-color: var(--ptg-background); color:#ffd75f; background-color:#ffd75f}
.ptg368 {background-color: var(--ptg-background); color:#af87ff; background-color:#afaf87}
.ptg369 {background-color: var(--ptg-background); color:#d78700; background-color:#ff00af}
.ptg370 {background-color: var(--ptg-background); color:#ffd7d7; background-color:#00d7ff}
.ptg371 {background-color: var(--ptg-background); color:#d7afff; background-color:#ff5faf}
.ptg372 {background-color: var(--ptg-background); color:#ffafff; background-color:#af00af}
.ptg373 {background-color: var(--ptg-background); color:#0000ff; background-color:#af87ff}
.ptg374 {background-color: var(--ptg-background); color:#d7afaf; background-color:#875faf}
.ptg375 {background-color: var(--ptg-background); color:#00d7ff; background-color:#ffaf87}
.ptg376 {background-color: var(--ptg-background); color:#d7ff5f; background-color:#87ffaf}
.ptg377 {background-color: var(--ptg-background); color:#af5f87; background-color:#ffd7d7}
.ptg378 {background-color: var(--ptg-background); color:#d75fff; background-color:#af8700}
.ptg379 {background-color: var(--ptg-background); color:#ff5f5f; background-color:#00afff}
.ptg380 {background-color: var(--ptg-background); color:#afff5f; background-color:#afaf00}
.ptg381 {background-color: var(--ptg-background); color:#5f00ff; background-color:#ff0087}
.ptg382 {background-color: var(--ptg-background); color:#af87ff; background-color:#878787}
.ptg383 {background-color: var(--ptg-background); color:#875fd7; background-color:#d7afaf}
.ptg384 {background-color: var(--ptg-background); color:#00af87; background-color:#ffafd7}
.ptg385 {background-color: var(--ptg-background); color:#5f5faf; background-color:#5f5fd7}
.ptg386 {background-color: var(--ptg-background); color:#5f5fff; background-color:#5f5faf}
.ptg387 {background-color: var(--ptg-background); color:#87d787; background-color:#5f87d7}
.ptg388 {background-color: var(--ptg-background); color:#ff5f5f; background-color:#d78787}
.ptg389 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#d78700}
.ptg390 {background-color: var(--ptg-background); color:#005faf; background-color:#d7ff87}
.ptg391 {background-color: var(--ptg-background); color:#875f00; background-color:#af8787}
.ptg392 {background-color: var(--ptg-background); color:#875faf; background-color:#5fff87}
.ptg393 {background-color: var(--ptg-background); color:#00ffff; background-color:#af875f}
.ptg394 {background-color: var(--ptg-background); color:#0087ff; background-color:#d787af}
.ptg395 {background-color: var(--ptg-background); color:#ff00af; background-color:#87afaf}
.ptg396 {background-color: var(--ptg-background); color:#d75fd7; background-color:#870000}
.ptg397 {background-color: var(--ptg-background); color:#5f00ff; background-color:#8787af}
.ptg398 {background-color: var(--ptg-background); color:#d700af; background-color:#d70087}
.ptg399 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#5f87ff}
.ptg400 {background-color: var(--ptg-background); color:#af00d7; background-color:#afff5f}
.ptg401 {background-color: var(--ptg-background); color:#005fff; background-color:#d7afff}
.ptg402 {background-color: var(--ptg-background); color:#afd7ff; background-color:#0000d7}
.ptg403 {background-color: var(--ptg-background); color:#8787ff; background-color:#8700ff}
.ptg404 {background-color: var(--ptg-background); color:#ff87af; background-color:#5fd75f}
.ptg405 {background-color: var(--ptg-background); color:#d75f87; background-color:#5fffaf}
.ptg406 {background-color: var(--ptg-background); color:#080808; background-color:#5f5fff}
.ptg407 {background-color: var(--ptg-background); color:#008700; background-color:#d7ff5f}
.ptg408 {background-color: var(--ptg-background); color:#afafd7; background-color:#000087}
.ptg409 {background-color: var(--ptg-background); color:#d7ffaf; background-color:#8700ff}
.ptg410 {background-color: var(--ptg-background); color:#5faf00; background-color:#5f5faf}
.ptg411 {background-color: var(--ptg-background); color:#d7af87; background-color:#00afd7}
.ptg412 {background-color: var(--ptg-background); color:#5f5faf; background-color:#ff87ff}
.ptg413 {background-color: var(--ptg-background); color:#5f0087; background-color:#00af00}
.ptg414 {background-color: var(--ptg-background); color:#d75f00; background-color:#5f00d7}
.ptg415 {background-color: var(--ptg-background); color:#d7d7d7; background-color:#5fffd7}
.ptg416 {background-color: var(--ptg-background); color:#00d787; background-color:#5f00af}
.ptg417 {background-color: var(--ptg-background); color:#5f5f00; background-color:#ff00af}
.ptg418 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#080808}
.ptg419 {background-color: var(--ptg-background); color:#d700ff; background-color:#af8787}
.ptg420 {background-color: var(--ptg-background); color:#d7ff5f; background-color:#5fafd7}
.ptg421 {background-color: var(--ptg-background); color:#00af87; background-color:#d7d7af}
.ptg422 {background-color: var(--ptg-background); color:#d75fff; background-color:#ff87af}
.ptg423 {background-color: var(--ptg-background); color:#d7afd7; background-color:#87afff}
.ptg424 {background-color: var(--ptg-background); color:#af00af; background-color:#af5faf}
.ptg425 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#af8787}
.ptg426 {background-color: var(--ptg-background); color:#ff5fff; background-color:#00afaf}
.ptg427 {background-color: var(--ptg-background); color:#87d7af; background-color:#ffd75f}
.ptg428 {background-color: var(--ptg-background); color:#af0000; background-color:#af875f}
.ptg429 {background-color: var(--ptg-background); color:#008700; background-color:#00afff}
.ptg430 {background-color: var(--ptg-background); color:#87ffd7; background-color:#5f8787}
.ptg431 {background-color: var(--ptg-background); color:#afafff; background-color:#00ff87}
.ptg432 {background-color: var(--ptg-background); color:#875fff; background-color:#ffaf00}
.ptg433 {background-color: var(--ptg-background); color:#875fd7; background-color:#ff8700}
.ptg434 {background-color: var(--ptg-background); color:#ff5f5f; background-color:#ff875f}
.ptg435 {background-color: var(--ptg-background); color:#005f5f; background-color:#87d7af}
.ptg436 {background-color: var(--ptg-background); color:#005fff; background-color:#87d7ff}
.ptg437 {background-color: var(--ptg-background); color:#87af5f; background-color:#ff5f00}
.ptg438 {background-color: var(--ptg-background); color:#af8787; background-color:#87ff87}
.ptg439 {background-color: var(--ptg-background); color:#ff5fff; background-color:#005f87}
.ptg440 {background-color: var(--ptg-background); color:#87ffd7; background-color:#d7d7ff}
.ptg441 {background-color: var(--ptg-background); color:#d7afaf; background-color:#af875f}
.ptg442 {background-color: var(--ptg-background); color:#d7005f; background-color:#afd7af}
.ptg443 {background-color: var(--ptg-background); color:#5f005f; background-color:#d75fd7}
.ptg444 {background-color: var(--ptg-background); color:#5f5fd7; background-color:#ffd787}
.ptg445 {background-color: var(--ptg-background); color:#5f0000; background-color:#5f00d7}
.ptg446 {background-color: var(--ptg-background); color:#00af5f; background-color:#87d7ff}
.ptg447 {background-color: var(--ptg-background); color:#5f5faf; background-color:#af87ff}
.ptg448 {background-color: var(--ptg-background); color: var(--ptg-background);; background-color: var(--ptg-foreground); background-color:#5f5faf; color:#af87ff}
    </style>
    <foreignObject width="100%" height="100%" x="0" y="0">
        <body xmlns="http://www.w3.org/1999/xhtml">
            <div id="ptg-terminal">
                <svg id="ptg-terminal-navbuttons" width="90" height="21"
                  viewBox="0 0 90 21" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="8" cy="6" r="6" fill="#ff6159"/>
                    <circle cx="28" cy="6" r="6" fill="#ffbd2e"/>
                    <circle cx="48" cy="6" r="6" fill="#28c941"/>
                </svg>
                <div id="ptg-terminal-title">PyTermGUI</div>
                <pre id="ptg-terminal-body">
                    <code>
<span class='ptg0'>▄</span><span class='ptg1'>▄</span><span class='ptg2'>▄</span><span class='ptg3'>▄</span><span class='ptg4'>▄</span><span class='ptg5'>▄</span><span class='ptg6'>▄</span><span class='ptg7'>▄</span><span class='ptg8'>▄</span><span class='ptg9'>▄</span><span class='ptg10'>▄</span><span class='ptg11'>▄</span><span class='ptg12'>▄</span><span class='ptg13'>▄</span><span class='ptg14'>▄</span><span class='ptg15'>▄</span><span class='ptg16'>▄</span><span class='ptg17'>▄</span><span class='ptg18'>▄</span><span class='ptg19'>▄</span><span class='ptg20'>▄</span><span class='ptg21'>▄</span><span class='ptg22'>▄</span><span class='ptg23'>▄</span><span class='ptg24'>▄</span><span class='ptg25'>▄</span><span class='ptg26'>▄</span><span class='ptg27'>▄</span><span class='ptg28'>▄</span><span class='ptg29'>▄</span>
<br /><span class='ptg30'>▄</span><span class='ptg31'>▄</span><span class='ptg32'>▄</span><span class='ptg33'>▄</span><span class='ptg34'>▄</span><span class='ptg35'>▄</span><span class='ptg36'>▄</span><span class='ptg37'>▄</span><span class='ptg38'>▄</span><span class='ptg39'>▄</span><span class='ptg40'>▄</span><span class='ptg41'>▄</span><span class='ptg42'>▄</span><span class='ptg43'>▄</span><span class='ptg44'>▄</span><span class='ptg45'>▄</span><span class='ptg46'>▄</span><span class='ptg47'>▄</span><span class='ptg48'>▄</span><span class='ptg49'>▄</span><span class='ptg50'>▄</span><span class='ptg51'>▄</span><span class='ptg52'>▄</span><span class='ptg53'>▄</span><span class='ptg54'>▄</span><span class='ptg55'>▄</span><span class='ptg56'>▄</span><span class='ptg57'>▄</span><span class='ptg58'>▄</span><span class='ptg59'>▄</span>
<br /><span class='ptg60'>▄</span><span class='ptg61'>▄</span><span class='ptg62'>▄</span><span class='ptg63'>▄</span><span class='ptg64'>▄</span><span class='ptg65'>▄</span><span class='ptg66'>▄</span><span class='ptg67'>▄</span><span class='ptg68'>▄</span><span class='ptg69'>▄</span><span class='ptg70'>▄</span><span class='ptg71'>▄</span><span class='ptg72'>▄</span><span class='ptg73'>▄</span><span class='ptg74'>▄</span><span class='ptg75'>▄</span><span class='ptg76'>▄</span><span class='ptg77'>▄</span><span class='ptg78'>▄</span><span class='ptg79'>▄</span><span class='ptg80'>▄</span><span class='ptg81'>▄</span><span class='ptg82'>▄</span><span class='ptg83'>▄</span><span class='ptg84'>▄</span><span class='ptg85'>▄</span><span class='ptg86'>▄</span><span class='ptg87'>▄</span><span class='ptg88'>▄</span><span class='ptg89'>▄</span>
<br /><span class='ptg90'>▄</span><span class='ptg91'>▄</span><span class='ptg92'>▄</span><span class='ptg93'>▄</span><span class='ptg94'>▄</span><span class='ptg95'>▄</span><span class='ptg96'>▄</span><span class='ptg97'>▄</span><span class='ptg98'>▄</span><span class='ptg99'>▄</span><span class='ptg100'>▄</span><span class='ptg101'>▄</span><span class='ptg102'>▄</span><span class='ptg103'>▄</span><span class='ptg104'>▄</span><span class='ptg105'>▄</span><span class='ptg106'>▄</span><span class='ptg107'>▄</span><span class='ptg108'>▄</span><span class='ptg109'>▄</span><span class='ptg110'>▄</span><span class='ptg111'>▄</span><span class='ptg112'>▄</span><span class='ptg113'>▄</span><span class='ptg114'>▄</span><span class='ptg115'>▄</span><span class='ptg116'>▄</span><span class='ptg117'>▄</span><span class='ptg118'>▄</span><span class='ptg119'>▄</span>
<br /><span class='ptg120'>▄</span><span class='ptg121'>▄</span><span class='ptg122'>▄</span><span class='ptg123'>▄</span><span class='ptg124'>▄</span><span class='ptg125'>▄</span><span class='ptg126'>▄</span><span class='ptg127'>▄</span><span class='ptg128'>▄</span><span class='ptg129'>▄</span><span class='ptg130'>▄</span><span class='ptg131'>▄</span><span class='ptg132'>▄</span><span class='ptg133'>▄</span><span class='ptg134'>▄</span><span class='ptg135'>▄</span><span class='ptg136'>▄</span><span class='ptg137'>▄</span><span class='ptg138'>▄</span><span class='ptg139'>▄</span><span class='ptg140'>▄</span><span class='ptg141'>▄</span><span class='ptg142'>▄</span><span class='ptg143'>▄</span><span class='ptg144'>▄</span><span class='ptg145'>▄</span><span class='ptg146'>▄</span><span class='ptg147'>▄</span><span class='ptg148'>▄</span><span class='ptg149'>▄</span>
<br /><span class='ptg150'>▄</span><span class='ptg151'>▄</span><span class='ptg152'>▄</span><span class='ptg153'>▄</span><span class='ptg154'>▄</span><span class='ptg155'>▄</span><span class='ptg156'>▄</span><span class='ptg157'>▄</span><span class='ptg158'>▄</span><span class='ptg159'>▄</span><span class='ptg160'>▄</span><span class='ptg161'>▄</span><span class='ptg162'>▄</span><span class='ptg163'>▄</span><span class='ptg164'>▄</span><span class='ptg165'>▄</span><span class='ptg166'>▄</span><span class='ptg167'>▄</span><span class='ptg168'>▄</span><span class='ptg169'>▄</span><span class='ptg170'>▄</span><span class='ptg171'>▄</span><span class='ptg172'>▄</span><span class='ptg173'>▄</span><span class='ptg174'>▄</span><span class='ptg175'>▄</span><span class='ptg176'>▄</span><span class='ptg177'>▄</span><span class='ptg178'>▄</span><span class='ptg179'>▄</span>
<br /><span class='ptg180'>▄</span><span class='ptg181'>▄</span><span class='ptg182'>▄</span><span class='ptg183'>▄</span><span class='ptg184'>▄</span><span class='ptg185'>▄</span><span class='ptg186'>▄</span><span class='ptg187'>▄</span><span class='ptg188'>▄</span><span class='ptg189'>▄</span><span class='ptg190'>▄</span><span class='ptg191'>▄</span><span class='ptg192'>▄</span><span class='ptg193'>▄</span><span class='ptg194'>▄</span><span class='ptg195'>▄</span><span class='ptg196'>▄</span><span class='ptg197'>▄</span><span class='ptg198'>▄</span><span class='ptg199'>▄</span><span class='ptg200'>▄</span><span class='ptg201'>▄</span><span class='ptg202'>▄</span><span class='ptg203'>▄</span><span class='ptg204'>▄</span><span class='ptg205'>▄</span><span class='ptg206'>▄</span><span class='ptg207'>▄</span><span class='ptg208'>▄</span><span class='ptg209'>▄</span>
<br /><span class='ptg210'>▄</span><span class='ptg211'>▄</span><span class='ptg212'>▄</span><span class='ptg213'>▄</span><span class='ptg214'>▄</span><span class='ptg215'>▄</span><span class='ptg216'>▄</span><span class='ptg217'>▄</span><span class='ptg218'>▄</span><span class='ptg219'>▄</span><span class='ptg220'>▄</span><span class='ptg221'>▄</span><span class='ptg222'>▄</span><span class='ptg223'>▄</span><span class='ptg224'>▄</span><span class='ptg225'>▄</span><span class='ptg226'>▄</span><span class='ptg227'>▄</span><span class='ptg228'>▄</span><span class='ptg229'>▄</span><span class='ptg230'>▄</span><span class='ptg231'>▄</span><span class='ptg232'>▄</span><span class='ptg233'>▄</span><span class='ptg234'>▄</span><span class='ptg235'>▄</span><span class='ptg236'>▄</span><span class='ptg237'>▄</span><span class='ptg238'>▄</span><span class='ptg239'>▄</span>
<br /><span class='ptg240'>▄</span><span class='ptg241'>▄</span><span class='ptg242'>▄</span><span class='ptg243'>▄</span><span class='ptg244'>▄</span><span class='ptg245'>▄</span><span class='ptg246'>▄</span><span class='ptg247'>▄</span><span class='ptg248'>▄</span><span class='ptg249'>▄</span><span class='ptg250'>▄</span><span class='ptg251'>▄</span><span class='ptg252'>▄</span><span class='ptg253'>▄</span><span class='ptg254'>▄</span><span class='ptg255'>▄</span><span class='ptg256'>▄</span><span class='ptg257'>▄</span><span class='ptg258'>▄</span><span class='ptg259'>▄</span><span class='ptg260'>▄</span><span class='ptg261'>▄</span><span class='ptg262'>▄</span><span class='ptg263'>▄</span><span class='ptg264'>▄</span><span class='ptg265'>▄</span><span class='ptg266'>▄</span><span class='ptg267'>▄</span><span class='ptg268'>▄</span><span class='ptg269'>▄</span>
<br /><span class='ptg270'>▄</span><span class='ptg271'>▄</span><span class='ptg272'>▄</span><span class='ptg273'>▄</span><span class='ptg37'>▄</span><span class='ptg274'>▄</span><span class='ptg275'>▄</span><span class='ptg276'>▄</span><span class='ptg277'>▄</span><span class='ptg278'>▄</span><span class='ptg279'>▄</span><span class='ptg280'>▄</span><span class='ptg281'>▄</span><span class='ptg282'>▄</span><span class='ptg283'>▄</span><span class='ptg284'>▄</span><span class='ptg285'>▄</span><span class='ptg286'>▄</span><span class='ptg287'>▄</span><span class='ptg288'>▄</span><span class='ptg289'>▄</span><span class='ptg290'>▄</span><span class='ptg291'>▄</span><span class='ptg292'>▄</span><span class='ptg293'>▄</span><span class='ptg294'>▄</span><span class='ptg295'>▄</span><span class='ptg296'>▄</span><span class='ptg297'>▄</span><span class='ptg298'>▄</span>
<br /><span class='ptg299'>▄</span><span class='ptg300'>▄</span><span class='ptg301'>▄</span><span class='ptg302'>▄</span><span class='ptg303'>▄</span><span class='ptg304'>▄</span><span class='ptg305'>▄</span><span class='ptg306'>▄</span><span class='ptg307'>▄</span><span class='ptg308'>▄</span><span class='ptg309'>▄</span><span class='ptg310'>▄</span><span class='ptg311'>▄</span><span class='ptg312'>▄</span><span class='ptg313'>▄</span><span class='ptg314'>▄</span><span class='ptg315'>▄</span><span class='ptg316'>▄</span><span class='ptg248'>▄</span><span class='ptg317'>▄</span><span class='ptg318'>▄</span><span class='ptg319'>▄</span><span class='ptg320'>▄</span><span class='ptg321'>▄</span><span class='ptg322'>▄</span><span class='ptg323'>▄</span><span class='ptg324'>▄</span><span class='ptg325'>▄</span><span class='ptg326'>▄</span><span class='ptg327'>▄</span>
<br /><span class='ptg328'>▄</span><span class='ptg329'>▄</span><span class='ptg330'>▄</span><span class='ptg331'>▄</span><span class='ptg332'>▄</span><span class='ptg333'>▄</span><span class='ptg334'>▄</span><span class='ptg335'>▄</span><span class='ptg336'>▄</span><span class='ptg337'>▄</span><span class='ptg338'>▄</span><span class='ptg339'>▄</span><span class='ptg340'>▄</span><span class='ptg341'>▄</span><span class='ptg342'>▄</span><span class='ptg337'>▄</span><span class='ptg343'>▄</span><span class='ptg344'>▄</span><span class='ptg345'>▄</span><span class='ptg346'>▄</span><span class='ptg347'>▄</span><span class='ptg348'>▄</span><span class='ptg349'>▄</span><span class='ptg350'>▄</span><span class='ptg351'>▄</span><span class='ptg352'>▄</span><span class='ptg353'>▄</span><span class='ptg354'>▄</span><span class='ptg355'>▄</span><span class='ptg356'>▄</span>
<br /><span class='ptg357'>▄</span><span class='ptg358'>▄</span><span class='ptg359'>▄</span><span class='ptg360'>▄</span><span class='ptg361'>▄</span><span class='ptg362'>▄</span><span class='ptg363'>▄</span><span class='ptg364'>▄</span><span class='ptg365'>▄</span><span class='ptg366'>▄</span><span class='ptg367'>▄</span><span class='ptg368'>▄</span><span class='ptg369'>▄</span><span class='ptg370'>▄</span><span class='ptg371'>▄</span><span class='ptg372'>▄</span><span class='ptg373'>▄</span><span class='ptg374'>▄</span><span class='ptg375'>▄</span><span class='ptg376'>▄</span><span class='ptg377'>▄</span><span class='ptg378'>▄</span><span class='ptg379'>▄</span><span class='ptg380'>▄</span><span class='ptg381'>▄</span><span class='ptg382'>▄</span><span class='ptg383'>▄</span><span class='ptg384'>▄</span><span class='ptg385'>▄</span><span class='ptg386'>▄</span>
<br /><span class='ptg387'>▄</span><span class='ptg388'>▄</span><span class='ptg389'>▄</span><span class='ptg390'>▄</span><span class='ptg391'>▄</span><span class='ptg392'>▄</span><span class='ptg393'>▄</span><span class='ptg394'>▄</span><span class='ptg395'>▄</span><span class='ptg396'>▄</span><span class='ptg397'>▄</span><span class='ptg398'>▄</span><span class='ptg399'>▄</span><span class='ptg400'>▄</span><span class='ptg401'>▄</span><span class='ptg402'>▄</span><span class='ptg403'>▄</span><span class='ptg404'>▄</span><span class='ptg405'>▄</span><span class='ptg406'>▄</span><span class='ptg407'>▄</span><span class='ptg408'>▄</span><span class='ptg409'>▄</span><span class='ptg410'>▄</span><span class='ptg411'>▄</span><span class='ptg412'>▄</span><span class='ptg413'>▄</span><span class='ptg414'>▄</span><span class='ptg415'>▄</span><span class='ptg416'>▄</span>
<br /><span class='ptg417'>▄</span><span class='ptg418'>▄</span><span class='ptg419'>▄</span><span class='ptg420'>▄</span><span class='ptg421'>▄</span><span class='ptg422'>▄</span><span class='ptg423'>▄</span><span class='ptg424'>▄</span><span class='ptg425'>▄</span><span class='ptg426'>▄</span><span class='ptg427'>▄</span><span class='ptg428'>▄</span><span class='ptg429'>▄</span><span class='ptg430'>▄</span><span class='ptg431'>▄</span><span class='ptg432'>▄</span><span class='ptg433'>▄</span><span class='ptg434'>▄</span><span class='ptg435'>▄</span><span class='ptg436'>▄</span><span class='ptg437'>▄</span><span class='ptg438'>▄</span><span class='ptg439'>▄</span><span class='ptg440'>▄</span><span class='ptg441'>▄</span><span class='ptg442'>▄</span><span class='ptg443'>▄</span><span class='ptg444'>▄</span><span class='ptg445'>▄</span><span class='ptg446'>▄</span>
<br /><span class='ptg447'>Hello</span><span class='ptg448'>There</span>
                    </code>
                </pre>
            </div>
        </body>
    </foreignObject>
</svg>"""

HTML_TARGET = """\
<html>
    <head>
        <style>
            body {
                --ptg-background: #000000;
                --ptg-foreground: #ffffff;
                color: var(--ptg-foreground);
                background-color: var(--ptg-background);
            }
            a {
                text-decoration: none;
                color: inherit;
            }
            code {
                font-size: 15px;
                font-family: Menlo, 'DejaVu Sans Mono', consolas, 'Courier New', monospace;
                line-height: 1.2em;
            }
            .ptg-position {
                position: absolute;
            }

.ptg0 {background-color: var(--ptg-background); color:#ffd787; background-color:#afaf00}
.ptg1 {background-color: var(--ptg-background); color:#5fff00; background-color:#875f87}
.ptg2 {background-color: var(--ptg-background); color:#afaf5f; background-color:#af87af}
.ptg3 {background-color: var(--ptg-background); color:#ff00af; background-color:#0087d7}
.ptg4 {background-color: var(--ptg-background); color:#ffd75f; background-color:#d7af5f}
.ptg5 {background-color: var(--ptg-background); color:#5faf00; background-color:#d7ff5f}
.ptg6 {background-color: var(--ptg-background); color:#5f005f; background-color:#ffaf00}
.ptg7 {background-color: var(--ptg-background); color:#00ffaf; background-color:#af00af}
.ptg8 {background-color: var(--ptg-background); color:#87ffd7; background-color:#ff87af}
.ptg9 {background-color: var(--ptg-background); color:#00af5f; background-color:#005faf}
.ptg10 {background-color: var(--ptg-background); color:#5f87ff; background-color:#8700ff}
.ptg11 {background-color: var(--ptg-background); color:#d70087; background-color:#5f5faf}
.ptg12 {background-color: var(--ptg-background); color:#d75f5f; background-color:#5f5f87}
.ptg13 {background-color: var(--ptg-background); color:#afafd7; background-color:#8787af}
.ptg14 {background-color: var(--ptg-background); color:#87d787; background-color:#87afaf}
.ptg15 {background-color: var(--ptg-background); color:#ff87ff; background-color:#afd787}
.ptg16 {background-color: var(--ptg-background); color:#d7d75f; background-color:#00af87}
.ptg17 {background-color: var(--ptg-background); color:#d75f5f; background-color:#d700ff}
.ptg18 {background-color: var(--ptg-background); color:#87ff00; background-color:#d7d7d7}
.ptg19 {background-color: var(--ptg-background); color:#5f5fd7; background-color:#8787af}
.ptg20 {background-color: var(--ptg-background); color:#ff0000; background-color:#5f00af}
.ptg21 {background-color: var(--ptg-background); color:#d75fd7; background-color:#d75f5f}
.ptg22 {background-color: var(--ptg-background); color:#00afd7; background-color:#ff87d7}
.ptg23 {background-color: var(--ptg-background); color:#ff5f87; background-color:#5f0000}
.ptg24 {background-color: var(--ptg-background); color:#8700d7; background-color:#afd7af}
.ptg25 {background-color: var(--ptg-background); color:#00ff5f; background-color:#87d787}
.ptg26 {background-color: var(--ptg-background); color:#ffafaf; background-color:#ff87ff}
.ptg27 {background-color: var(--ptg-background); color:#0000ff; background-color:#5f875f}
.ptg28 {background-color: var(--ptg-background); color:#00ffff; background-color:#5f5f00}
.ptg29 {background-color: var(--ptg-background); color:#d75f5f; background-color:#87875f}
.ptg30 {background-color: var(--ptg-background); color:#d78787; background-color:#d7af00}
.ptg31 {background-color: var(--ptg-background); color:#ff0000; background-color:#5fff5f}
.ptg32 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#d75f87}
.ptg33 {background-color: var(--ptg-background); color:#afd700; background-color:#ff87af}
.ptg34 {background-color: var(--ptg-background); color:#af5f00; background-color:#000087}
.ptg35 {background-color: var(--ptg-background); color:#af0087; background-color:#875f5f}
.ptg36 {background-color: var(--ptg-background); color:#005fff; background-color:#ffd787}
.ptg37 {background-color: var(--ptg-background); color:#00ffff; background-color:#5f0000}
.ptg38 {background-color: var(--ptg-background); color:#d7af87; background-color:#ff5faf}
.ptg39 {background-color: var(--ptg-background); color:#00ff5f; background-color:#d78700}
.ptg40 {background-color: var(--ptg-background); color:#afaf00; background-color:#5fff00}
.ptg41 {background-color: var(--ptg-background); color:#5f0087; background-color:#afafff}
.ptg42 {background-color: var(--ptg-background); color:#8787d7; background-color:#d7afaf}
.ptg43 {background-color: var(--ptg-background); color:#5f5fff; background-color:#d70087}
.ptg44 {background-color: var(--ptg-background); color:#0000ff; background-color:#87005f}
.ptg45 {background-color: var(--ptg-background); color:#5fffff; background-color:#ffff00}
.ptg46 {background-color: var(--ptg-background); color:#87d75f; background-color:#af8700}
.ptg47 {background-color: var(--ptg-background); color:#d7d787; background-color:#8700d7}
.ptg48 {background-color: var(--ptg-background); color:#afafd7; background-color:#008787}
.ptg49 {background-color: var(--ptg-background); color:#ff87d7; background-color:#5fff87}
.ptg50 {background-color: var(--ptg-background); color:#5f87ff; background-color:#5f8787}
.ptg51 {background-color: var(--ptg-background); color:#af5fd7; background-color:#d7afff}
.ptg52 {background-color: var(--ptg-background); color:#afffaf; background-color:#ffffaf}
.ptg53 {background-color: var(--ptg-background); color:#87d7d7; background-color:#878700}
.ptg54 {background-color: var(--ptg-background); color:#ffff00; background-color:#d70000}
.ptg55 {background-color: var(--ptg-background); color:#5f5fff; background-color:#5fff00}
.ptg56 {background-color: var(--ptg-background); color:#ff0087; background-color:#ffafd7}
.ptg57 {background-color: var(--ptg-background); color:#ffffff; background-color:#ffd7af}
.ptg58 {background-color: var(--ptg-background); color:#ffafff; background-color:#0087d7}
.ptg59 {background-color: var(--ptg-background); color:#ff00af; background-color:#afd7ff}
.ptg60 {background-color: var(--ptg-background); color:#00ff5f; background-color:#d7af00}
.ptg61 {background-color: var(--ptg-background); color:#00d7d7; background-color:#5f875f}
.ptg62 {background-color: var(--ptg-background); color:#000087; background-color:#00afff}
.ptg63 {background-color: var(--ptg-background); color:#00d7ff; background-color:#d7d7d7}
.ptg64 {background-color: var(--ptg-background); color:#d7d7d7; background-color:#ffff00}
.ptg65 {background-color: var(--ptg-background); color:#00ffaf; background-color:#5fafff}
.ptg66 {background-color: var(--ptg-background); color:#0087ff; background-color:#afffff}
.ptg67 {background-color: var(--ptg-background); color:#5f0000; background-color:#00d787}
.ptg68 {background-color: var(--ptg-background); color:#87ffff; background-color:#afaf5f}
.ptg69 {background-color: var(--ptg-background); color:#ff87af; background-color:#afff00}
.ptg70 {background-color: var(--ptg-background); color:#5fff87; background-color:#ffff87}
.ptg71 {background-color: var(--ptg-background); color:#ff8787; background-color:#d7af5f}
.ptg72 {background-color: var(--ptg-background); color:#afffff; background-color:#8787d7}
.ptg73 {background-color: var(--ptg-background); color:#d7ffff; background-color:#5fffaf}
.ptg74 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#af00d7}
.ptg75 {background-color: var(--ptg-background); color:#d78787; background-color:#00ff87}
.ptg76 {background-color: var(--ptg-background); color:#ff5fd7; background-color:#d7ffff}
.ptg77 {background-color: var(--ptg-background); color:#ffafff; background-color:#d7afff}
.ptg78 {background-color: var(--ptg-background); color:#ff8700; background-color:#00d7af}
.ptg79 {background-color: var(--ptg-background); color:#00005f; background-color:#005f00}
.ptg80 {background-color: var(--ptg-background); color:#ffd75f; background-color:#d7ff5f}
.ptg81 {background-color: var(--ptg-background); color:#d75f5f; background-color:#5f00af}
.ptg82 {background-color: var(--ptg-background); color:#875f00; background-color:#d7ff00}
.ptg83 {background-color: var(--ptg-background); color:#afffff; background-color:#5fffd7}
.ptg84 {background-color: var(--ptg-background); color:#0000ff; background-color:#0087af}
.ptg85 {background-color: var(--ptg-background); color:#d787af; background-color:#af87af}
.ptg86 {background-color: var(--ptg-background); color:#ffff00; background-color:#ffff87}
.ptg87 {background-color: var(--ptg-background); color:#afd75f; background-color:#5f00af}
.ptg88 {background-color: var(--ptg-background); color:#d70000; background-color:#87d7ff}
.ptg89 {background-color: var(--ptg-background); color:#d7af5f; background-color:#d7afd7}
.ptg90 {background-color: var(--ptg-background); color:#000087; background-color:#87afd7}
.ptg91 {background-color: var(--ptg-background); color:#ffd75f; background-color:#5f005f}
.ptg92 {background-color: var(--ptg-background); color:#5fffaf; background-color:#87ff87}
.ptg93 {background-color: var(--ptg-background); color:#5f00af; background-color:#af87af}
.ptg94 {background-color: var(--ptg-background); color:#af0087; background-color:#af00ff}
.ptg95 {background-color: var(--ptg-background); color:#ff8787; background-color:#87ffd7}
.ptg96 {background-color: var(--ptg-background); color:#005f5f; background-color:#d7d7ff}
.ptg97 {background-color: var(--ptg-background); color:#afaf00; background-color:#5faf87}
.ptg98 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#ff5faf}
.ptg99 {background-color: var(--ptg-background); color:#ffff87; background-color:#afd787}
.ptg100 {background-color: var(--ptg-background); color:#00ffaf; background-color:#afd75f}
.ptg101 {background-color: var(--ptg-background); color:#af00d7; background-color:#ff00af}
.ptg102 {background-color: var(--ptg-background); color:#5f00ff; background-color:#00d7d7}
.ptg103 {background-color: var(--ptg-background); color:#5fd7ff; background-color:#5f5f87}
.ptg104 {background-color: var(--ptg-background); color:#5fd7af; background-color:#5fffaf}
.ptg105 {background-color: var(--ptg-background); color:#87ff87; background-color:#0087ff}
.ptg106 {background-color: var(--ptg-background); color:#ffffff; background-color:#afafaf}
.ptg107 {background-color: var(--ptg-background); color:#87d700; background-color:#ff5fff}
.ptg108 {background-color: var(--ptg-background); color:#00afaf; background-color:#00afaf}
.ptg109 {background-color: var(--ptg-background); color:#87ffff; background-color:#870000}
.ptg110 {background-color: var(--ptg-background); color:#ffafd7; background-color:#5f005f}
.ptg111 {background-color: var(--ptg-background); color:#005f5f; background-color:#5faf00}
.ptg112 {background-color: var(--ptg-background); color:#af8787; background-color:#af87af}
.ptg113 {background-color: var(--ptg-background); color:#d75faf; background-color:#87d7af}
.ptg114 {background-color: var(--ptg-background); color:#87005f; background-color:#ff8700}
.ptg115 {background-color: var(--ptg-background); color:#5fffd7; background-color:#d7d75f}
.ptg116 {background-color: var(--ptg-background); color:#00af5f; background-color:#5fd7d7}
.ptg117 {background-color: var(--ptg-background); color:#d7ffaf; background-color:#d7005f}
.ptg118 {background-color: var(--ptg-background); color:#d7d700; background-color:#afaf00}
.ptg119 {background-color: var(--ptg-background); color:#af0087; background-color:#00d7ff}
.ptg120 {background-color: var(--ptg-background); color:#8700ff; background-color:#ff0087}
.ptg121 {background-color: var(--ptg-background); color:#5fff87; background-color:#afff00}
.ptg122 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#afffaf}
.ptg123 {background-color: var(--ptg-background); color:#87d7af; background-color:#af00ff}
.ptg124 {background-color: var(--ptg-background); color:#005f87; background-color:#ff00af}
.ptg125 {background-color: var(--ptg-background); color:#00ffaf; background-color:#5faf5f}
.ptg126 {background-color: var(--ptg-background); color:#af5f87; background-color:#87afaf}
.ptg127 {background-color: var(--ptg-background); color:#afffaf; background-color:#ffafaf}
.ptg128 {background-color: var(--ptg-background); color:#afd7af; background-color:#d7d787}
.ptg129 {background-color: var(--ptg-background); color:#afafaf; background-color:#8700af}
.ptg130 {background-color: var(--ptg-background); color:#afff00; background-color:#87af5f}
.ptg131 {background-color: var(--ptg-background); color:#5fafd7; background-color:#af005f}
.ptg132 {background-color: var(--ptg-background); color:#00d75f; background-color:#00af87}
.ptg133 {background-color: var(--ptg-background); color:#ffafd7; background-color:#afff87}
.ptg134 {background-color: var(--ptg-background); color:#5fff00; background-color:#ffafd7}
.ptg135 {background-color: var(--ptg-background); color:#d7af5f; background-color:#008787}
.ptg136 {background-color: var(--ptg-background); color:#005f87; background-color:#ffaf87}
.ptg137 {background-color: var(--ptg-background); color:#d7d787; background-color:#ffafd7}
.ptg138 {background-color: var(--ptg-background); color:#00d7ff; background-color:#87af00}
.ptg139 {background-color: var(--ptg-background); color:#875faf; background-color:#af00af}
.ptg140 {background-color: var(--ptg-background); color:#87afff; background-color:#d787af}
.ptg141 {background-color: var(--ptg-background); color:#ff8787; background-color:#875f5f}
.ptg142 {background-color: var(--ptg-background); color:#878700; background-color:#5f5faf}
.ptg143 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#d78787}
.ptg144 {background-color: var(--ptg-background); color:#87ff5f; background-color:#af0000}
.ptg145 {background-color: var(--ptg-background); color:#d7ffaf; background-color:#ff00d7}
.ptg146 {background-color: var(--ptg-background); color:#ffaf00; background-color:#5f0000}
.ptg147 {background-color: var(--ptg-background); color:#5f005f; background-color:#5faf87}
.ptg148 {background-color: var(--ptg-background); color:#005fff; background-color:#00ffaf}
.ptg149 {background-color: var(--ptg-background); color:#5f0087; background-color:#00875f}
.ptg150 {background-color: var(--ptg-background); color:#d70087; background-color:#000087}
.ptg151 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#d7af00}
.ptg152 {background-color: var(--ptg-background); color:#87d7d7; background-color:#d75fff}
.ptg153 {background-color: var(--ptg-background); color:#87d7af; background-color:#ffff87}
.ptg154 {background-color: var(--ptg-background); color:#ff87af; background-color:#d75f87}
.ptg155 {background-color: var(--ptg-background); color:#87875f; background-color:#afffaf}
.ptg156 {background-color: var(--ptg-background); color:#5fd787; background-color:#af5f5f}
.ptg157 {background-color: var(--ptg-background); color:#87afff; background-color:#afd787}
.ptg158 {background-color: var(--ptg-background); color:#00ffd7; background-color:#5faf5f}
.ptg159 {background-color: var(--ptg-background); color:#d75faf; background-color:#ffd787}
.ptg160 {background-color: var(--ptg-background); color:#5fffaf; background-color:#870000}
.ptg161 {background-color: var(--ptg-background); color:#00ffd7; background-color:#ffd700}
.ptg162 {background-color: var(--ptg-background); color:#ffaf87; background-color:#87ff5f}
.ptg163 {background-color: var(--ptg-background); color:#5fd787; background-color:#d7d7af}
.ptg164 {background-color: var(--ptg-background); color:#d7afff; background-color:#d70000}
.ptg165 {background-color: var(--ptg-background); color:#0087ff; background-color:#afd7af}
.ptg166 {background-color: var(--ptg-background); color:#ffd700; background-color:#87ff5f}
.ptg167 {background-color: var(--ptg-background); color:#afd7ff; background-color:#875f00}
.ptg168 {background-color: var(--ptg-background); color:#ffff87; background-color:#87ffaf}
.ptg169 {background-color: var(--ptg-background); color:#00afff; background-color:#ff5f87}
.ptg170 {background-color: var(--ptg-background); color:#af5f5f; background-color:#5f8787}
.ptg171 {background-color: var(--ptg-background); color:#5fd7ff; background-color:#870000}
.ptg172 {background-color: var(--ptg-background); color:#875fff; background-color:#5fafaf}
.ptg173 {background-color: var(--ptg-background); color:#ffd7af; background-color:#87d7af}
.ptg174 {background-color: var(--ptg-background); color:#ffff5f; background-color:#878787}
.ptg175 {background-color: var(--ptg-background); color:#d7af00; background-color:#87d7af}
.ptg176 {background-color: var(--ptg-background); color:#5f0087; background-color:#d7ff00}
.ptg177 {background-color: var(--ptg-background); color:#5f0000; background-color:#ff00d7}
.ptg178 {background-color: var(--ptg-background); color:#00afd7; background-color:#5f0000}
.ptg179 {background-color: var(--ptg-background); color:#ff875f; background-color:#5fafff}
.ptg180 {background-color: var(--ptg-background); color:#8787ff; background-color:#af00af}
.ptg181 {background-color: var(--ptg-background); color:#87af5f; background-color:#00d787}
.ptg182 {background-color: var(--ptg-background); color:#5fffd7; background-color:#af0000}
.ptg183 {background-color: var(--ptg-background); color:#af5f5f; background-color:#87af00}
.ptg184 {background-color: var(--ptg-background); color:#af87d7; background-color:#afaf00}
.ptg185 {background-color: var(--ptg-background); color:#af00af; background-color:#d7ff00}
.ptg186 {background-color: var(--ptg-background); color:#5f8700; background-color:#005f00}
.ptg187 {background-color: var(--ptg-background); color:#005f87; background-color:#080808}
.ptg188 {background-color: var(--ptg-background); color:#ffffd7; background-color:#87005f}
.ptg189 {background-color: var(--ptg-background); color:#0000af; background-color:#ffafaf}
.ptg190 {background-color: var(--ptg-background); color:#878700; background-color:#d7ff87}
.ptg191 {background-color: var(--ptg-background); color:#87af5f; background-color:#ff87ff}
.ptg192 {background-color: var(--ptg-background); color:#87d700; background-color:#87005f}
.ptg193 {background-color: var(--ptg-background); color:#ff5fff; background-color:#875f87}
.ptg194 {background-color: var(--ptg-background); color:#ffaf00; background-color:#5f005f}
.ptg195 {background-color: var(--ptg-background); color:#af0000; background-color:#87d75f}
.ptg196 {background-color: var(--ptg-background); color:#af00d7; background-color:#d75f87}
.ptg197 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#87ff5f}
.ptg198 {background-color: var(--ptg-background); color:#ff5f00; background-color:#87ff00}
.ptg199 {background-color: var(--ptg-background); color:#af5f5f; background-color:#5f5f5f}
.ptg200 {background-color: var(--ptg-background); color:#d7af87; background-color:#5fff5f}
.ptg201 {background-color: var(--ptg-background); color:#005faf; background-color:#d7d700}
.ptg202 {background-color: var(--ptg-background); color:#ff875f; background-color:#5fd75f}
.ptg203 {background-color: var(--ptg-background); color:#ff5fff; background-color:#87d700}
.ptg204 {background-color: var(--ptg-background); color:#87afd7; background-color:#5f5f87}
.ptg205 {background-color: var(--ptg-background); color:#af5f00; background-color:#d7af5f}
.ptg206 {background-color: var(--ptg-background); color:#5f87d7; background-color:#d7ffaf}
.ptg207 {background-color: var(--ptg-background); color:#0000af; background-color:#d75fd7}
.ptg208 {background-color: var(--ptg-background); color:#ffffff; background-color:#afafd7}
.ptg209 {background-color: var(--ptg-background); color:#af00d7; background-color:#afd700}
.ptg210 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#875f5f}
.ptg211 {background-color: var(--ptg-background); color:#af005f; background-color:#5fafff}
.ptg212 {background-color: var(--ptg-background); color:#d7d7ff; background-color:#5fff5f}
.ptg213 {background-color: var(--ptg-background); color:#ffff00; background-color:#d7af5f}
.ptg214 {background-color: var(--ptg-background); color:#008787; background-color:#d7d7af}
.ptg215 {background-color: var(--ptg-background); color:#5fd7ff; background-color:#875f00}
.ptg216 {background-color: var(--ptg-background); color:#ff0087; background-color:#5fafaf}
.ptg217 {background-color: var(--ptg-background); color:#080808; background-color:#ff00d7}
.ptg218 {background-color: var(--ptg-background); color:#00005f; background-color:#d7ffd7}
.ptg219 {background-color: var(--ptg-background); color:#00af5f; background-color:#ffd7d7}
.ptg220 {background-color: var(--ptg-background); color:#00afaf; background-color:#d7ffff}
.ptg221 {background-color: var(--ptg-background); color:#d7af87; background-color:#ffff00}
.ptg222 {background-color: var(--ptg-background); color:#87d7d7; background-color:#5f5faf}
.ptg223 {background-color: var(--ptg-background); color:#d70000; background-color:#d75f87}
.ptg224 {background-color: var(--ptg-background); color:#87d75f; background-color:#af00d7}
.ptg225 {background-color: var(--ptg-background); color:#d787af; background-color:#5f875f}
.ptg226 {background-color: var(--ptg-background); color:#00875f; background-color:#87ffff}
.ptg227 {background-color: var(--ptg-background); color:#5fd700; background-color:#8700d7}
.ptg228 {background-color: var(--ptg-background); color:#0087ff; background-color:#d7afff}
.ptg229 {background-color: var(--ptg-background); color:#00ff00; background-color:#d70000}
.ptg230 {background-color: var(--ptg-background); color:#d787af; background-color:#00afff}
.ptg231 {background-color: var(--ptg-background); color:#005fd7; background-color:#ffff5f}
.ptg232 {background-color: var(--ptg-background); color:#d7af00; background-color:#5faf00}
.ptg233 {background-color: var(--ptg-background); color:#00ff87; background-color:#00afaf}
.ptg234 {background-color: var(--ptg-background); color:#5f8787; background-color:#afffd7}
.ptg235 {background-color: var(--ptg-background); color:#5f8700; background-color:#ffd75f}
.ptg236 {background-color: var(--ptg-background); color:#008787; background-color:#afd7d7}
.ptg237 {background-color: var(--ptg-background); color:#ff87af; background-color:#870087}
.ptg238 {background-color: var(--ptg-background); color:#87ffff; background-color:#d787ff}
.ptg239 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#ffd7d7}
.ptg240 {background-color: var(--ptg-background); color:#d7d7ff; background-color:#ff5faf}
.ptg241 {background-color: var(--ptg-background); color:#d700ff; background-color:#d7af00}
.ptg242 {background-color: var(--ptg-background); color:#ffd7d7; background-color:#af00af}
.ptg243 {background-color: var(--ptg-background); color:#d7af87; background-color:#87ffff}
.ptg244 {background-color: var(--ptg-background); color:#af5faf; background-color:#87d700}
.ptg245 {background-color: var(--ptg-background); color:#00d7af; background-color:#ff875f}
.ptg246 {background-color: var(--ptg-background); color:#ff5f87; background-color:#af87ff}
.ptg247 {background-color: var(--ptg-background); color:#5fff5f; background-color:#0000af}
.ptg248 {background-color: var(--ptg-background); color:#5fd787; background-color:#875f00}
.ptg249 {background-color: var(--ptg-background); color:#5fff87; background-color:#ffafd7}
.ptg250 {background-color: var(--ptg-background); color:#875fff; background-color:#d75fd7}
.ptg251 {background-color: var(--ptg-background); color:#000087; background-color:#5faf5f}
.ptg252 {background-color: var(--ptg-background); color:#ff87d7; background-color:#d75f5f}
.ptg253 {background-color: var(--ptg-background); color:#afaf87; background-color:#5f5f5f}
.ptg254 {background-color: var(--ptg-background); color:#87ff87; background-color:#af5f5f}
.ptg255 {background-color: var(--ptg-background); color:#af5f00; background-color:#d7ff5f}
.ptg256 {background-color: var(--ptg-background); color:#87d700; background-color:#afafff}
.ptg257 {background-color: var(--ptg-background); color:#00ff5f; background-color:#5f0000}
.ptg258 {background-color: var(--ptg-background); color:#8787af; background-color:#005f00}
.ptg259 {background-color: var(--ptg-background); color:#8787af; background-color:#d7ffd7}
.ptg260 {background-color: var(--ptg-background); color:#875faf; background-color:#afd787}
.ptg261 {background-color: var(--ptg-background); color:#00ffd7; background-color:#005fd7}
.ptg262 {background-color: var(--ptg-background); color:#afaf5f; background-color:#875f5f}
.ptg263 {background-color: var(--ptg-background); color:#87afd7; background-color:#00af00}
.ptg264 {background-color: var(--ptg-background); color:#875f87; background-color:#ff87d7}
.ptg265 {background-color: var(--ptg-background); color:#5faf87; background-color:#878787}
.ptg266 {background-color: var(--ptg-background); color:#5fff5f; background-color:#87ffaf}
.ptg267 {background-color: var(--ptg-background); color:#af5f00; background-color:#5f8787}
.ptg268 {background-color: var(--ptg-background); color:#87afff; background-color:#af5f87}
.ptg269 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#00875f}
.ptg270 {background-color: var(--ptg-background); color:#5fd75f; background-color:#d7af87}
.ptg271 {background-color: var(--ptg-background); color:#d70087; background-color:#875f87}
.ptg272 {background-color: var(--ptg-background); color:#8700d7; background-color:#5f5fff}
.ptg273 {background-color: var(--ptg-background); color:#5f875f; background-color:#8700af}
.ptg274 {background-color: var(--ptg-background); color:#d7d787; background-color:#ffffaf}
.ptg275 {background-color: var(--ptg-background); color:#5f87d7; background-color:#8787d7}
.ptg276 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#00005f}
.ptg277 {background-color: var(--ptg-background); color:#d7d700; background-color:#d7ffff}
.ptg278 {background-color: var(--ptg-background); color:#afafaf; background-color:#ff87ff}
.ptg279 {background-color: var(--ptg-background); color:#ffafaf; background-color:#000087}
.ptg280 {background-color: var(--ptg-background); color:#af0087; background-color:#5fafd7}
.ptg281 {background-color: var(--ptg-background); color:#8787af; background-color:#d7d7d7}
.ptg282 {background-color: var(--ptg-background); color:#87afd7; background-color:#5fafd7}
.ptg283 {background-color: var(--ptg-background); color:#005f87; background-color:#5f87ff}
.ptg284 {background-color: var(--ptg-background); color:#005faf; background-color:#ff8787}
.ptg285 {background-color: var(--ptg-background); color:#00ff87; background-color:#ff5f87}
.ptg286 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#d7afff}
.ptg287 {background-color: var(--ptg-background); color:#5fafd7; background-color:#d75f00}
.ptg288 {background-color: var(--ptg-background); color:#ff87d7; background-color:#5faf5f}
.ptg289 {background-color: var(--ptg-background); color:#870000; background-color:#00d75f}
.ptg290 {background-color: var(--ptg-background); color:#afd787; background-color:#afffff}
.ptg291 {background-color: var(--ptg-background); color:#d7d787; background-color:#080808}
.ptg292 {background-color: var(--ptg-background); color:#00d75f; background-color:#af87ff}
.ptg293 {background-color: var(--ptg-background); color:#00ff87; background-color:#00d7ff}
.ptg294 {background-color: var(--ptg-background); color:#005f87; background-color:#af5fff}
.ptg295 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#d7005f}
.ptg296 {background-color: var(--ptg-background); color:#ffafaf; background-color:#ff005f}
.ptg297 {background-color: var(--ptg-background); color:#875f87; background-color:#878700}
.ptg298 {background-color: var(--ptg-background); color:#5f5faf; background-color:#ffff87}
.ptg299 {background-color: var(--ptg-background); color:#0000d7; background-color:#d75fd7}
.ptg300 {background-color: var(--ptg-background); color:#af87ff; background-color:#87ff5f}
.ptg301 {background-color: var(--ptg-background); color:#afaf00; background-color:#afd7af}
.ptg302 {background-color: var(--ptg-background); color:#ffff87; background-color:#5fd7d7}
.ptg303 {background-color: var(--ptg-background); color:#d75faf; background-color:#afffaf}
.ptg304 {background-color: var(--ptg-background); color:#00afff; background-color:#5fd75f}
.ptg305 {background-color: var(--ptg-background); color:#afd7af; background-color:#af00ff}
.ptg306 {background-color: var(--ptg-background); color:#0000ff; background-color:#d7afff}
.ptg307 {background-color: var(--ptg-background); color:#87d7ff; background-color:#00d7af}
.ptg308 {background-color: var(--ptg-background); color:#00d787; background-color:#d70087}
.ptg309 {background-color: var(--ptg-background); color:#00d787; background-color:#d75f5f}
.ptg310 {background-color: var(--ptg-background); color:#87afd7; background-color:#ffff00}
.ptg311 {background-color: var(--ptg-background); color:#d787af; background-color:#5f87af}
.ptg312 {background-color: var(--ptg-background); color:#ff5f00; background-color:#5fd75f}
.ptg313 {background-color: var(--ptg-background); color:#080808; background-color:#87d7ff}
.ptg314 {background-color: var(--ptg-background); color:#ff8787; background-color:#af5f87}
.ptg315 {background-color: var(--ptg-background); color:#af00ff; background-color:#875faf}
.ptg316 {background-color: var(--ptg-background); color:#5f00ff; background-color:#afd787}
.ptg317 {background-color: var(--ptg-background); color:#870000; background-color:#5fff87}
.ptg318 {background-color: var(--ptg-background); color:#ffff5f; background-color:#00d7ff}
.ptg319 {background-color: var(--ptg-background); color:#5f00af; background-color:#5f8787}
.ptg320 {background-color: var(--ptg-background); color:#5fd700; background-color:#ffd787}
.ptg321 {background-color: var(--ptg-background); color:#00af5f; background-color:#00ff5f}
.ptg322 {background-color: var(--ptg-background); color:#ffd7af; background-color:#ff87ff}
.ptg323 {background-color: var(--ptg-background); color:#87afff; background-color:#87d7ff}
.ptg324 {background-color: var(--ptg-background); color:#875f87; background-color:#ff0087}
.ptg325 {background-color: var(--ptg-background); color:#5fff00; background-color:#87ff5f}
.ptg326 {background-color: var(--ptg-background); color:#00ff5f; background-color:#d7afaf}
.ptg327 {background-color: var(--ptg-background); color:#ffd7d7; background-color:#5faf87}
.ptg328 {background-color: var(--ptg-background); color:#5fafaf; background-color:#d7ff00}
.ptg329 {background-color: var(--ptg-background); color:#87d75f; background-color:#af5fd7}
.ptg330 {background-color: var(--ptg-background); color:#87d7ff; background-color:#af5faf}
.ptg331 {background-color: var(--ptg-background); color:#af87ff; background-color:#d7ffaf}
.ptg332 {background-color: var(--ptg-background); color:#005f00; background-color:#ffd700}
.ptg333 {background-color: var(--ptg-background); color:#ffd700; background-color:#d78787}
.ptg334 {background-color: var(--ptg-background); color:#af5fff; background-color:#afffaf}
.ptg335 {background-color: var(--ptg-background); color:#5fff5f; background-color:#ff00d7}
.ptg336 {background-color: var(--ptg-background); color:#d7d75f; background-color:#00ff87}
.ptg337 {background-color: var(--ptg-background); color:#ff8787; background-color:#ffffff}
.ptg338 {background-color: var(--ptg-background); color:#005fd7; background-color:#afffaf}
.ptg339 {background-color: var(--ptg-background); color:#5fafd7; background-color:#ffff00}
.ptg340 {background-color: var(--ptg-background); color:#5f87af; background-color:#afff5f}
.ptg341 {background-color: var(--ptg-background); color:#ffff5f; background-color:#af00d7}
.ptg342 {background-color: var(--ptg-background); color:#af87af; background-color:#afaf87}
.ptg343 {background-color: var(--ptg-background); color:#080808; background-color:#00d7d7}
.ptg344 {background-color: var(--ptg-background); color:#870087; background-color:#5fafaf}
.ptg345 {background-color: var(--ptg-background); color:#d7ff87; background-color:#5fd7af}
.ptg346 {background-color: var(--ptg-background); color:#ffd7af; background-color:#ff87af}
.ptg347 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#afaf87}
.ptg348 {background-color: var(--ptg-background); color:#afaf00; background-color:#00875f}
.ptg349 {background-color: var(--ptg-background); color:#87d7ff; background-color:#00d7d7}
.ptg350 {background-color: var(--ptg-background); color:#ff875f; background-color:#00d7ff}
.ptg351 {background-color: var(--ptg-background); color:#d7d700; background-color:#d7af00}
.ptg352 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#ff87ff}
.ptg353 {background-color: var(--ptg-background); color:#ffafff; background-color:#87ffd7}
.ptg354 {background-color: var(--ptg-background); color:#5f5f5f; background-color:#875f87}
.ptg355 {background-color: var(--ptg-background); color:#afafaf; background-color:#ffffd7}
.ptg356 {background-color: var(--ptg-background); color:#ffaf00; background-color:#870087}
.ptg357 {background-color: var(--ptg-background); color:#af5fd7; background-color:#87875f}
.ptg358 {background-color: var(--ptg-background); color:#d7ff87; background-color:#ffaf87}
.ptg359 {background-color: var(--ptg-background); color:#5fafaf; background-color:#5fd7ff}
.ptg360 {background-color: var(--ptg-background); color:#00afff; background-color:#ff87d7}
.ptg361 {background-color: var(--ptg-background); color:#d75faf; background-color:#00005f}
.ptg362 {background-color: var(--ptg-background); color:#af0087; background-color:#d7ffd7}
.ptg363 {background-color: var(--ptg-background); color:#5fd7d7; background-color:#875f5f}
.ptg364 {background-color: var(--ptg-background); color:#0000af; background-color:#af875f}
.ptg365 {background-color: var(--ptg-background); color:#d7ff5f; background-color:#5fffd7}
.ptg366 {background-color: var(--ptg-background); color:#d7d700; background-color:#ff5fff}
.ptg367 {background-color: var(--ptg-background); color:#ffd75f; background-color:#ffd75f}
.ptg368 {background-color: var(--ptg-background); color:#af87ff; background-color:#afaf87}
.ptg369 {background-color: var(--ptg-background); color:#d78700; background-color:#ff00af}
.ptg370 {background-color: var(--ptg-background); color:#ffd7d7; background-color:#00d7ff}
.ptg371 {background-color: var(--ptg-background); color:#d7afff; background-color:#ff5faf}
.ptg372 {background-color: var(--ptg-background); color:#ffafff; background-color:#af00af}
.ptg373 {background-color: var(--ptg-background); color:#0000ff; background-color:#af87ff}
.ptg374 {background-color: var(--ptg-background); color:#d7afaf; background-color:#875faf}
.ptg375 {background-color: var(--ptg-background); color:#00d7ff; background-color:#ffaf87}
.ptg376 {background-color: var(--ptg-background); color:#d7ff5f; background-color:#87ffaf}
.ptg377 {background-color: var(--ptg-background); color:#af5f87; background-color:#ffd7d7}
.ptg378 {background-color: var(--ptg-background); color:#d75fff; background-color:#af8700}
.ptg379 {background-color: var(--ptg-background); color:#ff5f5f; background-color:#00afff}
.ptg380 {background-color: var(--ptg-background); color:#afff5f; background-color:#afaf00}
.ptg381 {background-color: var(--ptg-background); color:#5f00ff; background-color:#ff0087}
.ptg382 {background-color: var(--ptg-background); color:#af87ff; background-color:#878787}
.ptg383 {background-color: var(--ptg-background); color:#875fd7; background-color:#d7afaf}
.ptg384 {background-color: var(--ptg-background); color:#00af87; background-color:#ffafd7}
.ptg385 {background-color: var(--ptg-background); color:#5f5faf; background-color:#5f5fd7}
.ptg386 {background-color: var(--ptg-background); color:#5f5fff; background-color:#5f5faf}
.ptg387 {background-color: var(--ptg-background); color:#87d787; background-color:#5f87d7}
.ptg388 {background-color: var(--ptg-background); color:#ff5f5f; background-color:#d78787}
.ptg389 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#d78700}
.ptg390 {background-color: var(--ptg-background); color:#005faf; background-color:#d7ff87}
.ptg391 {background-color: var(--ptg-background); color:#875f00; background-color:#af8787}
.ptg392 {background-color: var(--ptg-background); color:#875faf; background-color:#5fff87}
.ptg393 {background-color: var(--ptg-background); color:#00ffff; background-color:#af875f}
.ptg394 {background-color: var(--ptg-background); color:#0087ff; background-color:#d787af}
.ptg395 {background-color: var(--ptg-background); color:#ff00af; background-color:#87afaf}
.ptg396 {background-color: var(--ptg-background); color:#d75fd7; background-color:#870000}
.ptg397 {background-color: var(--ptg-background); color:#5f00ff; background-color:#8787af}
.ptg398 {background-color: var(--ptg-background); color:#d700af; background-color:#d70087}
.ptg399 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#5f87ff}
.ptg400 {background-color: var(--ptg-background); color:#af00d7; background-color:#afff5f}
.ptg401 {background-color: var(--ptg-background); color:#005fff; background-color:#d7afff}
.ptg402 {background-color: var(--ptg-background); color:#afd7ff; background-color:#0000d7}
.ptg403 {background-color: var(--ptg-background); color:#8787ff; background-color:#8700ff}
.ptg404 {background-color: var(--ptg-background); color:#ff87af; background-color:#5fd75f}
.ptg405 {background-color: var(--ptg-background); color:#d75f87; background-color:#5fffaf}
.ptg406 {background-color: var(--ptg-background); color:#080808; background-color:#5f5fff}
.ptg407 {background-color: var(--ptg-background); color:#008700; background-color:#d7ff5f}
.ptg408 {background-color: var(--ptg-background); color:#afafd7; background-color:#000087}
.ptg409 {background-color: var(--ptg-background); color:#d7ffaf; background-color:#8700ff}
.ptg410 {background-color: var(--ptg-background); color:#5faf00; background-color:#5f5faf}
.ptg411 {background-color: var(--ptg-background); color:#d7af87; background-color:#00afd7}
.ptg412 {background-color: var(--ptg-background); color:#5f5faf; background-color:#ff87ff}
.ptg413 {background-color: var(--ptg-background); color:#5f0087; background-color:#00af00}
.ptg414 {background-color: var(--ptg-background); color:#d75f00; background-color:#5f00d7}
.ptg415 {background-color: var(--ptg-background); color:#d7d7d7; background-color:#5fffd7}
.ptg416 {background-color: var(--ptg-background); color:#00d787; background-color:#5f00af}
.ptg417 {background-color: var(--ptg-background); color:#5f5f00; background-color:#ff00af}
.ptg418 {background-color: var(--ptg-background); color:#d7ffd7; background-color:#080808}
.ptg419 {background-color: var(--ptg-background); color:#d700ff; background-color:#af8787}
.ptg420 {background-color: var(--ptg-background); color:#d7ff5f; background-color:#5fafd7}
.ptg421 {background-color: var(--ptg-background); color:#00af87; background-color:#d7d7af}
.ptg422 {background-color: var(--ptg-background); color:#d75fff; background-color:#ff87af}
.ptg423 {background-color: var(--ptg-background); color:#d7afd7; background-color:#87afff}
.ptg424 {background-color: var(--ptg-background); color:#af00af; background-color:#af5faf}
.ptg425 {background-color: var(--ptg-background); color:#ffaf5f; background-color:#af8787}
.ptg426 {background-color: var(--ptg-background); color:#ff5fff; background-color:#00afaf}
.ptg427 {background-color: var(--ptg-background); color:#87d7af; background-color:#ffd75f}
.ptg428 {background-color: var(--ptg-background); color:#af0000; background-color:#af875f}
.ptg429 {background-color: var(--ptg-background); color:#008700; background-color:#00afff}
.ptg430 {background-color: var(--ptg-background); color:#87ffd7; background-color:#5f8787}
.ptg431 {background-color: var(--ptg-background); color:#afafff; background-color:#00ff87}
.ptg432 {background-color: var(--ptg-background); color:#875fff; background-color:#ffaf00}
.ptg433 {background-color: var(--ptg-background); color:#875fd7; background-color:#ff8700}
.ptg434 {background-color: var(--ptg-background); color:#ff5f5f; background-color:#ff875f}
.ptg435 {background-color: var(--ptg-background); color:#005f5f; background-color:#87d7af}
.ptg436 {background-color: var(--ptg-background); color:#005fff; background-color:#87d7ff}
.ptg437 {background-color: var(--ptg-background); color:#87af5f; background-color:#ff5f00}
.ptg438 {background-color: var(--ptg-background); color:#af8787; background-color:#87ff87}
.ptg439 {background-color: var(--ptg-background); color:#ff5fff; background-color:#005f87}
.ptg440 {background-color: var(--ptg-background); color:#87ffd7; background-color:#d7d7ff}
.ptg441 {background-color: var(--ptg-background); color:#d7afaf; background-color:#af875f}
.ptg442 {background-color: var(--ptg-background); color:#d7005f; background-color:#afd7af}
.ptg443 {background-color: var(--ptg-background); color:#5f005f; background-color:#d75fd7}
.ptg444 {background-color: var(--ptg-background); color:#5f5fd7; background-color:#ffd787}
.ptg445 {background-color: var(--ptg-background); color:#5f0000; background-color:#5f00d7}
.ptg446 {background-color: var(--ptg-background); color:#00af5f; background-color:#87d7ff}
.ptg447 {background-color: var(--ptg-background); color:#5f5faf; background-color:#af87ff}
.ptg448 {background-color: var(--ptg-background); color: var(--ptg-background);; background-color: var(--ptg-foreground); background-color:#5f5faf; color:#af87ff}
        </style>
    </head>
    <body>
        <pre class="ptg">
            <code>
<span class='ptg0'>▄</span><span class='ptg1'>▄</span><span class='ptg2'>▄</span><span class='ptg3'>▄</span><span class='ptg4'>▄</span><span class='ptg5'>▄</span><span class='ptg6'>▄</span><span class='ptg7'>▄</span><span class='ptg8'>▄</span><span class='ptg9'>▄</span><span class='ptg10'>▄</span><span class='ptg11'>▄</span><span class='ptg12'>▄</span><span class='ptg13'>▄</span><span class='ptg14'>▄</span><span class='ptg15'>▄</span><span class='ptg16'>▄</span><span class='ptg17'>▄</span><span class='ptg18'>▄</span><span class='ptg19'>▄</span><span class='ptg20'>▄</span><span class='ptg21'>▄</span><span class='ptg22'>▄</span><span class='ptg23'>▄</span><span class='ptg24'>▄</span><span class='ptg25'>▄</span><span class='ptg26'>▄</span><span class='ptg27'>▄</span><span class='ptg28'>▄</span><span class='ptg29'>▄</span>
<span class='ptg30'>▄</span><span class='ptg31'>▄</span><span class='ptg32'>▄</span><span class='ptg33'>▄</span><span class='ptg34'>▄</span><span class='ptg35'>▄</span><span class='ptg36'>▄</span><span class='ptg37'>▄</span><span class='ptg38'>▄</span><span class='ptg39'>▄</span><span class='ptg40'>▄</span><span class='ptg41'>▄</span><span class='ptg42'>▄</span><span class='ptg43'>▄</span><span class='ptg44'>▄</span><span class='ptg45'>▄</span><span class='ptg46'>▄</span><span class='ptg47'>▄</span><span class='ptg48'>▄</span><span class='ptg49'>▄</span><span class='ptg50'>▄</span><span class='ptg51'>▄</span><span class='ptg52'>▄</span><span class='ptg53'>▄</span><span class='ptg54'>▄</span><span class='ptg55'>▄</span><span class='ptg56'>▄</span><span class='ptg57'>▄</span><span class='ptg58'>▄</span><span class='ptg59'>▄</span>
<span class='ptg60'>▄</span><span class='ptg61'>▄</span><span class='ptg62'>▄</span><span class='ptg63'>▄</span><span class='ptg64'>▄</span><span class='ptg65'>▄</span><span class='ptg66'>▄</span><span class='ptg67'>▄</span><span class='ptg68'>▄</span><span class='ptg69'>▄</span><span class='ptg70'>▄</span><span class='ptg71'>▄</span><span class='ptg72'>▄</span><span class='ptg73'>▄</span><span class='ptg74'>▄</span><span class='ptg75'>▄</span><span class='ptg76'>▄</span><span class='ptg77'>▄</span><span class='ptg78'>▄</span><span class='ptg79'>▄</span><span class='ptg80'>▄</span><span class='ptg81'>▄</span><span class='ptg82'>▄</span><span class='ptg83'>▄</span><span class='ptg84'>▄</span><span class='ptg85'>▄</span><span class='ptg86'>▄</span><span class='ptg87'>▄</span><span class='ptg88'>▄</span><span class='ptg89'>▄</span>
<span class='ptg90'>▄</span><span class='ptg91'>▄</span><span class='ptg92'>▄</span><span class='ptg93'>▄</span><span class='ptg94'>▄</span><span class='ptg95'>▄</span><span class='ptg96'>▄</span><span class='ptg97'>▄</span><span class='ptg98'>▄</span><span class='ptg99'>▄</span><span class='ptg100'>▄</span><span class='ptg101'>▄</span><span class='ptg102'>▄</span><span class='ptg103'>▄</span><span class='ptg104'>▄</span><span class='ptg105'>▄</span><span class='ptg106'>▄</span><span class='ptg107'>▄</span><span class='ptg108'>▄</span><span class='ptg109'>▄</span><span class='ptg110'>▄</span><span class='ptg111'>▄</span><span class='ptg112'>▄</span><span class='ptg113'>▄</span><span class='ptg114'>▄</span><span class='ptg115'>▄</span><span class='ptg116'>▄</span><span class='ptg117'>▄</span><span class='ptg118'>▄</span><span class='ptg119'>▄</span>
<span class='ptg120'>▄</span><span class='ptg121'>▄</span><span class='ptg122'>▄</span><span class='ptg123'>▄</span><span class='ptg124'>▄</span><span class='ptg125'>▄</span><span class='ptg126'>▄</span><span class='ptg127'>▄</span><span class='ptg128'>▄</span><span class='ptg129'>▄</span><span class='ptg130'>▄</span><span class='ptg131'>▄</span><span class='ptg132'>▄</span><span class='ptg133'>▄</span><span class='ptg134'>▄</span><span class='ptg135'>▄</span><span class='ptg136'>▄</span><span class='ptg137'>▄</span><span class='ptg138'>▄</span><span class='ptg139'>▄</span><span class='ptg140'>▄</span><span class='ptg141'>▄</span><span class='ptg142'>▄</span><span class='ptg143'>▄</span><span class='ptg144'>▄</span><span class='ptg145'>▄</span><span class='ptg146'>▄</span><span class='ptg147'>▄</span><span class='ptg148'>▄</span><span class='ptg149'>▄</span>
<span class='ptg150'>▄</span><span class='ptg151'>▄</span><span class='ptg152'>▄</span><span class='ptg153'>▄</span><span class='ptg154'>▄</span><span class='ptg155'>▄</span><span class='ptg156'>▄</span><span class='ptg157'>▄</span><span class='ptg158'>▄</span><span class='ptg159'>▄</span><span class='ptg160'>▄</span><span class='ptg161'>▄</span><span class='ptg162'>▄</span><span class='ptg163'>▄</span><span class='ptg164'>▄</span><span class='ptg165'>▄</span><span class='ptg166'>▄</span><span class='ptg167'>▄</span><span class='ptg168'>▄</span><span class='ptg169'>▄</span><span class='ptg170'>▄</span><span class='ptg171'>▄</span><span class='ptg172'>▄</span><span class='ptg173'>▄</span><span class='ptg174'>▄</span><span class='ptg175'>▄</span><span class='ptg176'>▄</span><span class='ptg177'>▄</span><span class='ptg178'>▄</span><span class='ptg179'>▄</span>
<span class='ptg180'>▄</span><span class='ptg181'>▄</span><span class='ptg182'>▄</span><span class='ptg183'>▄</span><span class='ptg184'>▄</span><span class='ptg185'>▄</span><span class='ptg186'>▄</span><span class='ptg187'>▄</span><span class='ptg188'>▄</span><span class='ptg189'>▄</span><span class='ptg190'>▄</span><span class='ptg191'>▄</span><span class='ptg192'>▄</span><span class='ptg193'>▄</span><span class='ptg194'>▄</span><span class='ptg195'>▄</span><span class='ptg196'>▄</span><span class='ptg197'>▄</span><span class='ptg198'>▄</span><span class='ptg199'>▄</span><span class='ptg200'>▄</span><span class='ptg201'>▄</span><span class='ptg202'>▄</span><span class='ptg203'>▄</span><span class='ptg204'>▄</span><span class='ptg205'>▄</span><span class='ptg206'>▄</span><span class='ptg207'>▄</span><span class='ptg208'>▄</span><span class='ptg209'>▄</span>
<span class='ptg210'>▄</span><span class='ptg211'>▄</span><span class='ptg212'>▄</span><span class='ptg213'>▄</span><span class='ptg214'>▄</span><span class='ptg215'>▄</span><span class='ptg216'>▄</span><span class='ptg217'>▄</span><span class='ptg218'>▄</span><span class='ptg219'>▄</span><span class='ptg220'>▄</span><span class='ptg221'>▄</span><span class='ptg222'>▄</span><span class='ptg223'>▄</span><span class='ptg224'>▄</span><span class='ptg225'>▄</span><span class='ptg226'>▄</span><span class='ptg227'>▄</span><span class='ptg228'>▄</span><span class='ptg229'>▄</span><span class='ptg230'>▄</span><span class='ptg231'>▄</span><span class='ptg232'>▄</span><span class='ptg233'>▄</span><span class='ptg234'>▄</span><span class='ptg235'>▄</span><span class='ptg236'>▄</span><span class='ptg237'>▄</span><span class='ptg238'>▄</span><span class='ptg239'>▄</span>
<span class='ptg240'>▄</span><span class='ptg241'>▄</span><span class='ptg242'>▄</span><span class='ptg243'>▄</span><span class='ptg244'>▄</span><span class='ptg245'>▄</span><span class='ptg246'>▄</span><span class='ptg247'>▄</span><span class='ptg248'>▄</span><span class='ptg249'>▄</span><span class='ptg250'>▄</span><span class='ptg251'>▄</span><span class='ptg252'>▄</span><span class='ptg253'>▄</span><span class='ptg254'>▄</span><span class='ptg255'>▄</span><span class='ptg256'>▄</span><span class='ptg257'>▄</span><span class='ptg258'>▄</span><span class='ptg259'>▄</span><span class='ptg260'>▄</span><span class='ptg261'>▄</span><span class='ptg262'>▄</span><span class='ptg263'>▄</span><span class='ptg264'>▄</span><span class='ptg265'>▄</span><span class='ptg266'>▄</span><span class='ptg267'>▄</span><span class='ptg268'>▄</span><span class='ptg269'>▄</span>
<span class='ptg270'>▄</span><span class='ptg271'>▄</span><span class='ptg272'>▄</span><span class='ptg273'>▄</span><span class='ptg37'>▄</span><span class='ptg274'>▄</span><span class='ptg275'>▄</span><span class='ptg276'>▄</span><span class='ptg277'>▄</span><span class='ptg278'>▄</span><span class='ptg279'>▄</span><span class='ptg280'>▄</span><span class='ptg281'>▄</span><span class='ptg282'>▄</span><span class='ptg283'>▄</span><span class='ptg284'>▄</span><span class='ptg285'>▄</span><span class='ptg286'>▄</span><span class='ptg287'>▄</span><span class='ptg288'>▄</span><span class='ptg289'>▄</span><span class='ptg290'>▄</span><span class='ptg291'>▄</span><span class='ptg292'>▄</span><span class='ptg293'>▄</span><span class='ptg294'>▄</span><span class='ptg295'>▄</span><span class='ptg296'>▄</span><span class='ptg297'>▄</span><span class='ptg298'>▄</span>
<span class='ptg299'>▄</span><span class='ptg300'>▄</span><span class='ptg301'>▄</span><span class='ptg302'>▄</span><span class='ptg303'>▄</span><span class='ptg304'>▄</span><span class='ptg305'>▄</span><span class='ptg306'>▄</span><span class='ptg307'>▄</span><span class='ptg308'>▄</span><span class='ptg309'>▄</span><span class='ptg310'>▄</span><span class='ptg311'>▄</span><span class='ptg312'>▄</span><span class='ptg313'>▄</span><span class='ptg314'>▄</span><span class='ptg315'>▄</span><span class='ptg316'>▄</span><span class='ptg248'>▄</span><span class='ptg317'>▄</span><span class='ptg318'>▄</span><span class='ptg319'>▄</span><span class='ptg320'>▄</span><span class='ptg321'>▄</span><span class='ptg322'>▄</span><span class='ptg323'>▄</span><span class='ptg324'>▄</span><span class='ptg325'>▄</span><span class='ptg326'>▄</span><span class='ptg327'>▄</span>
<span class='ptg328'>▄</span><span class='ptg329'>▄</span><span class='ptg330'>▄</span><span class='ptg331'>▄</span><span class='ptg332'>▄</span><span class='ptg333'>▄</span><span class='ptg334'>▄</span><span class='ptg335'>▄</span><span class='ptg336'>▄</span><span class='ptg337'>▄</span><span class='ptg338'>▄</span><span class='ptg339'>▄</span><span class='ptg340'>▄</span><span class='ptg341'>▄</span><span class='ptg342'>▄</span><span class='ptg337'>▄</span><span class='ptg343'>▄</span><span class='ptg344'>▄</span><span class='ptg345'>▄</span><span class='ptg346'>▄</span><span class='ptg347'>▄</span><span class='ptg348'>▄</span><span class='ptg349'>▄</span><span class='ptg350'>▄</span><span class='ptg351'>▄</span><span class='ptg352'>▄</span><span class='ptg353'>▄</span><span class='ptg354'>▄</span><span class='ptg355'>▄</span><span class='ptg356'>▄</span>
<span class='ptg357'>▄</span><span class='ptg358'>▄</span><span class='ptg359'>▄</span><span class='ptg360'>▄</span><span class='ptg361'>▄</span><span class='ptg362'>▄</span><span class='ptg363'>▄</span><span class='ptg364'>▄</span><span class='ptg365'>▄</span><span class='ptg366'>▄</span><span class='ptg367'>▄</span><span class='ptg368'>▄</span><span class='ptg369'>▄</span><span class='ptg370'>▄</span><span class='ptg371'>▄</span><span class='ptg372'>▄</span><span class='ptg373'>▄</span><span class='ptg374'>▄</span><span class='ptg375'>▄</span><span class='ptg376'>▄</span><span class='ptg377'>▄</span><span class='ptg378'>▄</span><span class='ptg379'>▄</span><span class='ptg380'>▄</span><span class='ptg381'>▄</span><span class='ptg382'>▄</span><span class='ptg383'>▄</span><span class='ptg384'>▄</span><span class='ptg385'>▄</span><span class='ptg386'>▄</span>
<span class='ptg387'>▄</span><span class='ptg388'>▄</span><span class='ptg389'>▄</span><span class='ptg390'>▄</span><span class='ptg391'>▄</span><span class='ptg392'>▄</span><span class='ptg393'>▄</span><span class='ptg394'>▄</span><span class='ptg395'>▄</span><span class='ptg396'>▄</span><span class='ptg397'>▄</span><span class='ptg398'>▄</span><span class='ptg399'>▄</span><span class='ptg400'>▄</span><span class='ptg401'>▄</span><span class='ptg402'>▄</span><span class='ptg403'>▄</span><span class='ptg404'>▄</span><span class='ptg405'>▄</span><span class='ptg406'>▄</span><span class='ptg407'>▄</span><span class='ptg408'>▄</span><span class='ptg409'>▄</span><span class='ptg410'>▄</span><span class='ptg411'>▄</span><span class='ptg412'>▄</span><span class='ptg413'>▄</span><span class='ptg414'>▄</span><span class='ptg415'>▄</span><span class='ptg416'>▄</span>
<span class='ptg417'>▄</span><span class='ptg418'>▄</span><span class='ptg419'>▄</span><span class='ptg420'>▄</span><span class='ptg421'>▄</span><span class='ptg422'>▄</span><span class='ptg423'>▄</span><span class='ptg424'>▄</span><span class='ptg425'>▄</span><span class='ptg426'>▄</span><span class='ptg427'>▄</span><span class='ptg428'>▄</span><span class='ptg429'>▄</span><span class='ptg430'>▄</span><span class='ptg431'>▄</span><span class='ptg432'>▄</span><span class='ptg433'>▄</span><span class='ptg434'>▄</span><span class='ptg435'>▄</span><span class='ptg436'>▄</span><span class='ptg437'>▄</span><span class='ptg438'>▄</span><span class='ptg439'>▄</span><span class='ptg440'>▄</span><span class='ptg441'>▄</span><span class='ptg442'>▄</span><span class='ptg443'>▄</span><span class='ptg444'>▄</span><span class='ptg445'>▄</span><span class='ptg446'>▄</span>
<span class='ptg447'>Hello</span><span class='ptg448'>There</span>
            </code>
        </pre>
    </body>
</html>"""
