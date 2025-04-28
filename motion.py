from moviepy.editor import *
from moviepy.video.fx import resize

# Carrega a imagem
imagem = ImageClip("sua_imagem.png")

# Define a duração do vídeo (20 segundos)
imagem = imagem.set_duration(20)

# Aplica o efeito Ken Burns (zoom + movimento)
motion = imagem.fx(resize.resize, lambda t: 1 + 0.05 * (t / 20))

# Move levemente a imagem para cima (efeito panorâmico)
motion = motion.set_position(lambda t: ("center", int(30 * (t / 20))))

# Ajusta o tamanho para 720p
motion = motion.resize(height=720)

# Exporta o vídeo final
motion.write_videofile("video_output.mp4", fps=24)
