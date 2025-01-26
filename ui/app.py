import gradio as gr
import cv2
import numpy as np
from src.core.resize import ImageResizer
from src.core.adjust import ImageAdjuster
from src.core.enhance import ImageEnhancer
from src.ai.remove_bg import BackgroundRemover
from src.ai.lighting import LightingAdjuster
import sys
sys.path.append('..')  # 添加父目錄到路徑

from src.core.resize import ImageResizer

def process_image(image, resize_width, resize_height, aspect_ratio,
                brightness, contrast, saturation, sharpness,
                denoise_strength, remove_bg, auto_lighting):
   
   if resize_width or resize_height:
       image = ImageResizer.resize_image(image, resize_width, resize_height)
   
   if aspect_ratio != "原始比例":
       image = ImageResizer.crop_image(image, aspect_ratio)
       
   if brightness != 0:
       image = ImageAdjuster.adjust_brightness(image, brightness)
   if contrast != 0:
       image = ImageAdjuster.adjust_contrast(image, contrast)
   if saturation != 0:
       image = ImageAdjuster.adjust_saturation(image, saturation)
       
   if sharpness > 0:
       image = ImageEnhancer.sharpen(image, sharpness)
   if denoise_strength > 0:
       image = ImageEnhancer.denoise(image, denoise_strength)
       
   if remove_bg:
       image = BackgroundRemover.remove_background(image)
   if auto_lighting:
       image = LightingAdjuster.auto_lighting(image)
   
   return image

with gr.Blocks() as demo:
   gr.Markdown("# Casper 圖片處理工具 🎨")
   
   with gr.Tabs():
       with gr.Tab("基礎處理"):
           with gr.Row():
               with gr.Column():
                   input_image = gr.Image(label="上傳圖片")
                   
                   with gr.Group():
                       gr.Markdown("### 基本設定")
                       with gr.Row():
                           resize_width = gr.Number(label="寬度", value=0)
                           resize_height = gr.Number(label="高度", value=0)
                       aspect_ratio = gr.Dropdown(
                           choices=["原始比例", "1:1", "4:3", "16:9"],
                           value="原始比例",
                           label="裁切比例"
                       )
                       
                       gr.Markdown("### 調整參數")
                       brightness = gr.Slider(-100, 100, 0, label="亮度")
                       contrast = gr.Slider(-100, 100, 0, label="對比度")
                       saturation = gr.Slider(-100, 100, 0, label="飽和度")
                       sharpness = gr.Slider(0, 100, 0, label="銳利度")
                       denoise_strength = gr.Slider(0, 20, 0, label="降噪強度")
                       remove_bg = gr.Checkbox(label="移除背景")
                       auto_lighting = gr.Checkbox(label="自動補光")
                   
                   process_btn = gr.Button("處理圖片")
                   
               with gr.Column():
                   output_image = gr.Image(label="處理結果")
        # 第二頁：特效處理
       with gr.Tab("特效處理"):
           with gr.Row():
               with gr.Column():
                   effect_input = gr.Image(label="上傳圖片", elem_id="image-tools")
               with gr.Column():
                   effect_output = gr.Image(label="特效結果", elem_id="image-tools")
           
           with gr.Row():
               gr.Markdown("### 特效選項")
               # 這裡可以添加特效相關的控制項
   
   process_btn.click(fn=process_image,
                    inputs=[input_image, resize_width, resize_height, 
                           aspect_ratio, brightness, contrast,
                           saturation, sharpness, denoise_strength,
                           remove_bg, auto_lighting],
                    outputs=output_image)

demo.launch()