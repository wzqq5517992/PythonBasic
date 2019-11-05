flower = "{ @}"
# row = 1
# while row <= 5:
#     print(flower * row)
#     row += 1
#
# role_list = ["{ @}", " *"]
#
# print(",".join(str(i) for i in role_list))


# row = 1
# while row <= 5:
#     col = 1
#     while col <= row:
#         print(flower, end=" *")
#
#         col += 1
#     print("")
#
#     row += 1

flowers = [
    "         { @}", "      { @} *{ @}",
    "   { @} *{ @} *{ @}", "{ @} *{ @} *{ @} *{ @}",
    "\ *{ @} *{ @} *{ @} /", "    \ \ \ z / / /",
    "     \\ \  c / //", "      \ \ l //",
    "       \ \y //","        >= <",
    "       /    \\"

]

for flowers_str in flowers:
    print("%s" % flowers_str.center(10, " "), )
