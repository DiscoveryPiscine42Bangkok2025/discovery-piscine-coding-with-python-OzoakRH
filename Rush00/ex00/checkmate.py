def checkmate(board_str: str):
#รับ board เป็นสตริงหลายบรรทัด (แต่ละบรรทัดคือแถว)
#แล้วก็ถ้า "Success" หาก King ถูก check, "Fail" ถ้าไม่ถูก check,
#หรือ "Error" ถ้า input ผิดรูปแบบ

  if board_str is None:
    print("Error")
    return
# แยกเป็นแถว และตัดบรรทัดที่ว่างส่วนเกินข้างหน้า/ข้างหลัง
  rows = board_str.splitline()
# กำจัดบรรทัดว่างที่เกิดจาก leading/trailing newlines
  rows = [r for r in rows if r != ""]

  if not rows:
      print("Error")
      return

  n = len(row)
  # ต้องเป็นตารางจัตุรัส: ทุกแถวต้องมีความยาว n
  for r in rows:
      if len(r) != n:
          print("Error")
          return

  # หา King
  king_count = 0
  kr = kc = -1
  for i, r in enumerate(rows):
      for j, ch in enumerate(r):
          if ch == 'K':
              king_count += 1
              kr, kc = i, j
