from checkmate import checkmate

def main():
    #จะแสดงตัวอย่างบอร์ด 4x4
    board_4x4 = """\
....
.K..
..P.
....\
""" # K อยู่ที่ (1,1) และ เบี้ย หรือ Pawn อยุ่ที่ (2,2) (Pawn อยู่ใต้ King มุมขวา -> check K)
    print("=== 4x4 board ===")
    print(board_4x4)
    print("Result:")
    checkmate(board_4x4)
