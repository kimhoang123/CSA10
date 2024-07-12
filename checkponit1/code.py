import pygame

class TroChoi:
    def __init__(self, canvas):
        self.canvas = canvas
        self.thoi_gian = 30  # tgian ban dau la 30s
        self.mau_nen_ket_thuc = (0, 0, 0)  # background color

    def dem_nguoc(self):
        self.thoi_gian -= 1 / 60
        if self.thoi_gian < 25:
            self.ket_thuc()

    def hien_thi_thoi_gian(self):
        if self.thoi_gian > 25:
            if pygame.font:
                font = pygame.font.Font(None, 36)
                chuoi_thoi_gian = font.render(f"Time: {self.thoi_gian:.2f} giây", 1, (255, 255, 255))
                self.canvas.blit(chuoi_thoi_gian, (0, 0))

    def ket_thuc(self):
        self.canvas.fill(self.mau_nen_ket_thuc)
        if pygame.font:
            font = pygame.font.Font(None, 36)
            chuoi_ket_thuc = font.render("END GAME", 1, (255, 255, 255))
            self.canvas.blit(chuoi_ket_thuc, (275, 280))

# Ví dụ sử dụng
pygame.init()
canvas = pygame.display.set_mode((640, 480))
trochoi = TroChoi(canvas)

# Vòng lặp
running = True
dongho = pygame.time.Clock()

while running:
    for su_kien in pygame.event.get(): # lặp các skieen như nhấn phím, di chuyển chuột, hoặc đóng cửa sổ.
        if su_kien.type == pygame.QUIT:
            running = False

    trochoi.dem_nguoc()
    trochoi.hien_thi_thoi_gian()

    pygame.display.flip()

pygame.quit()
