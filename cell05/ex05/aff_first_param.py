import sys
# ตรวจสอบว่าจำนวนอาร์กิวเมนต์ที่ส่งมามีมากกว่า 1 มั้ย
if len(sys.argv) > 1:
    # ถ้ามี ให้พิมพ์อาร์กิวเมนต์ตัวแรก (ที่ index 1)
    print(sys.argv[1])
else:
    print('none')
