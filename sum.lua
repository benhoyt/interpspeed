-- time lua sum.lua
local s = 0
for i = 0, 100000000-1 do
    s = s + i
end
print(s)
