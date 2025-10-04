import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox, ttk, scrolledtext
import re
import os
import json
import time
import math
import threading
from datetime import datetime
from collections import deque
import statistics
import pygame

# Enhanced imports with better error handling
try:
    from deep_translator import GoogleTranslator
    TRANSLATION_AVAILABLE = True
except ImportError:
    TRANSLATION_AVAILABLE = False
    print("🌐 Translation: Install 'deep-translator' for AI translation")

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    print("🎤 Voice: Install 'SpeechRecognition' for voice features")

try:
    from gtts import gTTS
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("🔊 TTS: Install 'gtts' for text-to-speech")

try:
    from docx import Document
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False
    print("📄 DOCX: Install 'python-docx' for Word document support")

class UltimateAITeleprompter:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨🚀 ULTIMATE AI TELEPROMPTER 4000 - COLOR EDITION")
        self.root.configure(bg='#0a0a0a')
        self.root.geometry("1800x1000")
        
        # AI Configuration
        self.config_file = "ai_teleprompter_config.json"
        self.translation_cache = {}
        self.performance_data = deque(maxlen=100)
        
        # 🎨 COMPREHENSIVE COLOR SYSTEM
        self.current_theme = "matrix"
        self.themes = {
            "matrix": {
                "bg": "#000000",           # Main background
                "text": "#00ff00",         # Primary text color
                "highlight": "#ffff00",    # Highlight color
                "accent": "#ff00ff",       # Accent color
                "ui_bg": "#1a1a1a",       # UI background
                "progress": "#00ff00",     # Progress bar color
                "button_bg": "#006600",    # Button background
                "button_fg": "#ffffff",    # Button text color
                "canvas_bg": "#000000",    # Canvas background
                "status_bg": "#1a1a1a",    # Status bar background
                "border": "#00ff00",       # Border color
                "warning": "#ff3333",      # Warning color
                "success": "#00ff00",      # Success color
                "info": "#00ffff"          # Info color
            },
            "cyber": {
                "bg": "#0a0a2a", 
                "text": "#00ffff", 
                "highlight": "#ff00ff", 
                "accent": "#ffff00", 
                "ui_bg": "#1a1a2a",
                "progress": "#00ffff",
                "button_bg": "#0044cc",
                "button_fg": "#ffffff",
                "canvas_bg": "#0a0a2a",
                "status_bg": "#1a1a2a",
                "border": "#00ffff",
                "warning": "#ff4444",
                "success": "#00ffff",
                "info": "#ff00ff"
            },
            "sunset": {
                "bg": "#1a002a", 
                "text": "#ff6b6b", 
                "highlight": "#ffd93d", 
                "accent": "#6bcf7f", 
                "ui_bg": "#2a1a3a",
                "progress": "#ff6b6b",
                "button_bg": "#cc5500",
                "button_fg": "#ffffff",
                "canvas_bg": "#1a002a",
                "status_bg": "#2a1a3a",
                "border": "#ff6b6b",
                "warning": "#ff3333",
                "success": "#6bcf7f",
                "info": "#ffd93d"
            },
            "ocean": {
                "bg": "#001a33", 
                "text": "#4ecdc4", 
                "highlight": "#ff6b6b", 
                "accent": "#45b7d1", 
                "ui_bg": "#1a2a3a",
                "progress": "#4ecdc4",
                "button_bg": "#0066cc",
                "button_fg": "#ffffff",
                "canvas_bg": "#001a33",
                "status_bg": "#1a2a3a",
                "border": "#4ecdc4",
                "warning": "#ff6b6b",
                "success": "#4ecdc4",
                "info": "#45b7d1"
            },
            "forest": {
                "bg": "#0a2a1a", 
                "text": "#6bcf7f", 
                "highlight": "#ffd93d", 
                "accent": "#4ecdc4", 
                "ui_bg": "#1a2a1a",
                "progress": "#6bcf7f",
                "button_bg": "#006600",
                "button_fg": "#ffffff",
                "canvas_bg": "#0a2a1a",
                "status_bg": "#1a2a1a",
                "border": "#6bcf7f",
                "warning": "#ff6b6b",
                "success": "#6bcf7f",
                "info": "#ffd93d"
            },
            "fire": {
                "bg": "#2a0a0a", 
                "text": "#ff6b6b", 
                "highlight": "#ffd93d", 
                "accent": "#ff8e42", 
                "ui_bg": "#3a1a1a",
                "progress": "#ff6b6b",
                "button_bg": "#cc3300",
                "button_fg": "#ffffff",
                "canvas_bg": "#2a0a0a",
                "status_bg": "#3a1a1a",
                "border": "#ff6b6b",
                "warning": "#ff3333",
                "success": "#ff8e42",
                "info": "#ffd93d"
            },
            "galaxy": {
                "bg": "#0a0a1a", 
                "text": "#9d4edd", 
                "highlight": "#ff6b6b", 
                "accent": "#4cc9f0", 
                "ui_bg": "#1a1a2a",
                "progress": "#9d4edd",
                "button_bg": "#6600cc",
                "button_fg": "#ffffff",
                "canvas_bg": "#0a0a1a",
                "status_bg": "#1a1a2a",
                "border": "#9d4edd",
                "warning": "#ff6b6b",
                "success": "#4cc9f0",
                "info": "#9d4edd"
            },
            "neon": {
                "bg": "#000000", 
                "text": "#ff00ff", 
                "highlight": "#00ffff", 
                "accent": "#ffff00", 
                "ui_bg": "#1a001a",
                "progress": "#ff00ff",
                "button_bg": "#cc00cc",
                "button_fg": "#ffffff",
                "canvas_bg": "#000000",
                "status_bg": "#1a001a",
                "border": "#ff00ff",
                "warning": "#ff3333",
                "success": "#00ffff",
                "info": "#ffff00"
            },
            "gold": {
                "bg": "#1a1400", 
                "text": "#ffd700", 
                "highlight": "#ff6b6b", 
                "accent": "#c0c0c0", 
                "ui_bg": "#2a2400",
                "progress": "#ffd700",
                "button_bg": "#cc9900",
                "button_fg": "#000000",
                "canvas_bg": "#1a1400",
                "status_bg": "#2a2400",
                "border": "#ffd700",
                "warning": "#ff6b6b",
                "success": "#ffd700",
                "info": "#c0c0c0"
            },
            "ice": {
                "bg": "#001a33", 
                "text": "#e0f7ff", 
                "highlight": "#4ecdc4", 
                "accent": "#87ceeb", 
                "ui_bg": "#002b4d",
                "progress": "#4ecdc4",
                "button_bg": "#0066cc",
                "button_fg": "#ffffff",
                "canvas_bg": "#001a33",
                "status_bg": "#002b4d",
                "border": "#4ecdc4",
                "warning": "#ff6b6b",
                "success": "#4ecdc4",
                "info": "#87ceeb"
            }
        }
        
        # Initialize with default theme colors
        theme = self.themes[self.current_theme]
        self.bg_color = theme["bg"]
        self.text_color = theme["text"]
        self.highlight_color = theme["highlight"]
        self.accent_color = theme["accent"]
        self.ui_bg_color = theme["ui_bg"]
        self.progress_color = theme["progress"]
        self.button_bg = theme["button_bg"]
        self.button_fg = theme["button_fg"]
        self.canvas_bg = theme["canvas_bg"]
        self.status_bg = theme["status_bg"]
        self.border_color = theme["border"]
        self.warning_color = theme["warning"]
        self.success_color = theme["success"]
        self.info_color = theme["info"]
        
        # AI-Powered Variables
        self.scroll_delay = tk.IntVar(value=10)  # Faster default speed
        self.scroll_step = tk.DoubleVar(value=5.0)  # Larger step
        self.font_size = tk.IntVar(value=48)
        self.font_family = "Consolas"
        
        # AI Modes
        self.mode = tk.StringVar(value="AI Adaptive")
        self.auto_pause = tk.BooleanVar(value=True)
        self.pause_duration = tk.IntVar(value=1000)
        self.current_language = tk.StringVar(value="en")
        self.target_language = tk.StringVar(value="es")
        self.show_timer = tk.BooleanVar(value=True)
        self.mirror_mode = tk.BooleanVar(value=False)
        self.reading_speed = tk.IntVar(value=250)
        self.translate_mode = tk.BooleanVar(value=False)
        self.voice_control = tk.BooleanVar(value=False)
        self.auto_scroll = tk.BooleanVar(value=True)
        self.show_translation = tk.BooleanVar(value=False)
        self.ai_adaptive_speed = tk.BooleanVar(value=True)
        self.eye_tracking_sim = tk.BooleanVar(value=False)
        self.sentiment_analysis = tk.BooleanVar(value=False)
        
        # Enhanced AI Languages Database
        self.languages = {
            'en': 'English', 'es': 'Spanish', 'fr': 'French', 'de': 'German',
            'it': 'Italian', 'pt': 'Portuguese', 'ru': 'Russian', 'zh': 'Chinese',
            'ja': 'Japanese', 'ko': 'Korean', 'ar': 'Arabic', 'hi': 'Hindi',
            'tr': 'Turkish', 'nl': 'Dutch', 'pl': 'Polish', 'sv': 'Swedish',
            'vi': 'Vietnamese', 'th': 'Thai', 'id': 'Indonesian', 'ms': 'Malay',
            'fil': 'Filipino', 'sw': 'Swahili', 'he': 'Hebrew', 'el': 'Greek',
            'da': 'Danish', 'fi': 'Finnish', 'no': 'Norwegian', 'cs': 'Czech',
            'hu': 'Hungarian', 'ro': 'Romanian', 'sk': 'Slovak', 'bg': 'Bulgarian',
            'uk': 'Ukrainian', 'hr': 'Croatian', 'sr': 'Serbian', 'sl': 'Slovenian'
        }
        
        # AI State Management
        self.text_id = None
        self.translation_id = None
        self.text_y = 0
        self.translation_y = 0
        self.original_content = """🎨🚀 WELCOME TO ULTIMATE AI TELEPROMPTER 4000 - COLOR EDITION

🌈 REVOLUTIONARY COLOR FEATURES:
• 🎨 10 VIBRANT COLOR THEMES
• 🌈 Dynamic Color Coordination
• 🎯 Smart Color Highlighting
• 💫 Smooth Color Transitions
• 🎭 Professional Visual Design

🌟 AI-POWERED FEATURES:
• 🤖 AI-Powered Adaptive Speed Control
• 🌐 Real-time Multi-language Translation
• 🎙 Advanced Voice Recognition & Synthesis
• 📊 Live Performance Analytics Dashboard
• 🎮 Professional Broadcasting Controls
• ⚡ Real-time Progress Tracking
• 🔄 Smart Content Highlighting

💡 GETTING STARTED:
1. Load your script using the AI File Manager
2. Choose your preferred Color Theme
3. Select AI mode and settings
4. Start your presentation with one click!

🎯 PRO TIP: Different themes work best for different presentation types!"""
        self.text_content = self.original_content
        self.translated_content = ""
        self.text_sentences = []
        self.translated_sentences = []
        self.sentence_index = 0
        self.word_index = 0
        self.word_list = []
        self.scrolling = False
        self.files = []
        self.current_file_index = 0
        self.is_translating = False
        self.translation_active = False
        
        # AI Analytics
        self.session_start_time = None
        self.words_read = 0
        self.total_session_time = 0
        self.reading_sessions = []
        self.performance_metrics = {
            'avg_wpm': 0,
            'consistency': 0,
            'focus_score': 0,
            'improvement_trend': 0
        }
        
        # Enhanced Audio System
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            self.audio_available = True
        except:
            self.audio_available = False
            print("🔊 Audio: Pygame mixer initialization failed")
        
        self.is_speaking = False
        
        # Enhanced Speech Recognition
        if SPEECH_RECOGNITION_AVAILABLE:
            try:
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
                self.voice_available = True
                print("🎤 Voice: Speech recognition initialized successfully")
            except:
                self.voice_available = False
                print("🎤 Voice: Microphone not available")
        else:
            self.voice_available = False
        
        # Initialize AI Systems
        self.setup_ai_ui()
        self.load_ai_config()
        self.setup_ai_keyboard_shortcuts()
        self.process_ai_content()
        self.start_ai_background_services()

    def setup_ai_ui(self):
        # Create futuristic notebook with enhanced styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=self.ui_bg_color)
        style.configure('TNotebook.Tab', 
                       background=self.ui_bg_color, 
                       foreground=self.text_color,
                       padding=[20, 5],
                       font=('Arial', 10, 'bold'))
        style.map('TNotebook.Tab', 
                 background=[('selected', self.accent_color)],
                 foreground=[('selected', '#ffffff')])
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create all tabs
        self.main_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.main_frame, text="🎨 AI TELEPROMPTER")
        
        self.control_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.control_frame, text="⚡ CONTROL CENTER")
        
        self.analytics_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.analytics_frame, text="📊 AI DASHBOARD")
        
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="🔧 AI SETTINGS")
        
        # Setup each tab
        self.setup_ai_teleprompter_tab()
        self.setup_ai_control_center()
        self.setup_ai_analytics_dashboard()
        self.setup_ai_settings()

    def setup_ai_teleprompter_tab(self):
        # AI Header with enhanced styling
        header_frame = tk.Frame(self.main_frame, bg=self.ui_bg_color, height=80)
        header_frame.pack(fill='x', padx=5, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, 
                              text="🎨🚀 ULTIMATE AI TELEPROMPTER 4000 - COLOR EDITION", 
                              font=("Arial", 20, "bold"), 
                              fg=self.text_color, 
                              bg=self.ui_bg_color)
        title_label.pack(side='left', padx=20, pady=20)
        
        self.status_label = tk.Label(header_frame, 
                                    text="🟢 AI SYSTEM READY", 
                                    font=("Arial", 12, "bold"), 
                                    fg=self.success_color, 
                                    bg=self.ui_bg_color)
        self.status_label.pack(side='right', padx=20, pady=20)
        
        # Theme indicator
        self.theme_label = tk.Label(header_frame, 
                                   text=f"🎨 {self.current_theme.upper()}", 
                                   font=("Arial", 10, "bold"), 
                                   fg=self.accent_color, 
                                   bg=self.ui_bg_color)
        self.theme_label.pack(side='right', padx=10, pady=20)
        
        # Dual Canvas System for Translation
        canvas_container = tk.Frame(self.main_frame, bg=self.bg_color)
        canvas_container.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Main Teleprompter Canvas (Left - Original Text)
        self.canvas = tk.Canvas(canvas_container, 
                               bg=self.canvas_bg, 
                               highlightthickness=3, 
                               highlightbackground=self.border_color,
                               cursor="crosshair")
        self.canvas.pack(side='left', fill='both', expand=True, padx=(0, 2))
        
        # Add canvas label with theme colors
        self.canvas_label_left = tk.Label(self.canvas, text="ORIGINAL TEXT", 
                                   bg=self.canvas_bg, fg=self.text_color,
                                   font=("Arial", 10, "bold"))
        self.canvas_label_left.place(x=50, y=10)
        
        # Translation Canvas (Right - Translated Text)
        self.translation_canvas = tk.Canvas(canvas_container, 
                                           bg=self.canvas_bg, 
                                           highlightthickness=3,
                                           highlightbackground=self.highlight_color,
                                           cursor="crosshair")
        
        # Initially hide translation canvas until translation is activated
        self.translation_canvas.pack_forget()
        
        # AI Status Bar
        self.setup_ai_status_bar()

    def setup_ai_status_bar(self):
        status_bar = tk.Frame(self.main_frame, bg=self.status_bg, height=50)
        status_bar.pack(fill='x', padx=5, pady=2)
        status_bar.pack_propagate(False)
        
        # Left Status - Performance Metrics
        left_status = tk.Frame(status_bar, bg=self.status_bg)
        left_status.pack(side='left')
        
        self.timer_label = tk.Label(left_status, 
                                   text="🕒 00:00:00", 
                                   fg=self.text_color, 
                                   bg=self.status_bg, 
                                   font=("Arial", 10, "bold"))
        self.timer_label.pack(side='left', padx=10)
        
        self.wpm_label = tk.Label(left_status, 
                                 text="⚡ WPM: 0", 
                                 fg=self.highlight_color, 
                                 bg=self.status_bg, 
                                 font=("Arial", 10, "bold"))
        self.wpm_label.pack(side='left', padx=10)
        
        self.focus_label = tk.Label(left_status, 
                                   text="🎯 Focus: 100%", 
                                   fg=self.accent_color, 
                                   bg=self.status_bg, 
                                   font=("Arial", 10, "bold"))
        self.focus_label.pack(side='left', padx=10)
        
        # Center Progress - AI Enhanced
        center_status = tk.Frame(status_bar, bg=self.status_bg)
        center_status.pack(side='left', expand=True, fill='x', padx=20)
        
        # Progress bar with custom style
        style = ttk.Style()
        style.configure("Custom.Horizontal.TProgressbar", 
                       troughcolor='#333333', 
                       background=self.progress_color,
                       thickness=20)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(center_status, 
                                           variable=self.progress_var, 
                                           length=400, 
                                           style='Custom.Horizontal.TProgressbar')
        self.progress_bar.pack(pady=5)
        
        # Progress Labels
        progress_frame = tk.Frame(center_status, bg=self.status_bg)
        progress_frame.pack(fill='x')
        
        self.progress_text = tk.Label(progress_frame, 
                                     text="0% • 0/0 words • Est: 0m 0s", 
                                     fg=self.info_color, 
                                     bg=self.status_bg, 
                                     font=("Arial", 9, "bold"))
        self.progress_text.pack()
        
        # Right Status - System Info
        right_status = tk.Frame(status_bar, bg=self.status_bg)
        right_status.pack(side='right')
        
        self.mode_label = tk.Label(right_status, 
                                  text="🤖 AI Adaptive Mode", 
                                  fg=self.text_color, 
                                  bg=self.status_bg, 
                                  font=("Arial", 10, "bold"))
        self.mode_label.pack(side='right', padx=10)
        
        self.file_label = tk.Label(right_status, 
                                  text="📁 No file loaded", 
                                  fg=self.highlight_color, 
                                  bg=self.status_bg, 
                                  font=("Arial", 10))
        self.file_label.pack(side='right', padx=10)
        
        # Translation Status
        self.translation_status = tk.Label(right_status, 
                                         text="🌐 Translation: OFF", 
                                         fg=self.info_color, 
                                         bg=self.status_bg, 
                                         font=("Arial", 9))
        self.translation_status.pack(side='right', padx=10)

    def setup_ai_control_center(self):
        # Main control container
        main_container = tk.Frame(self.control_frame, bg=self.bg_color)
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # File Operations Section
        file_section = self.create_section(main_container, "📁 AI FILE MANAGER", 0)
        self.create_file_controls(file_section)
        
        # Playback Controls Section
        playback_section = self.create_section(main_container, "🎮 PLAYBACK CONTROL", 1)
        self.create_playback_controls(playback_section)
        
        # AI Features Section
        features_section = self.create_section(main_container, "🤖 AI FEATURES", 2)
        self.create_ai_features(features_section)
        
        # Quick Settings Section
        settings_section = self.create_section(main_container, "⚡ QUICK SETTINGS", 3)
        self.create_quick_settings(settings_section)

    def create_section(self, parent, title, row):
        """Create a standardized section frame"""
        section = tk.LabelFrame(parent, text=title, 
                              fg=self.text_color, 
                              bg=self.ui_bg_color,
                              font=("Arial", 12, "bold"), 
                              padx=15, pady=15,
                              relief='raised', 
                              bd=2,
                              highlightbackground=self.border_color,
                              highlightcolor=self.border_color)
        section.grid(row=row, column=0, sticky='ew', padx=10, pady=10)
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        return section

    def create_file_controls(self, parent):
        """Create file operation controls with theme colors"""
        file_buttons = [
            ("🚀 LOAD DOCUMENT", self.load_file, self.button_bg, self.button_fg),
            ("📂 LOAD MULTIPLE", self.load_multiple_files, self.accent_color, self.button_fg),
            ("💾 SAVE SCRIPT", self.save_script, self.highlight_color, '#000000'),
            ("📝 NEW SCRIPT", self.new_script, self.info_color, self.button_fg),
            ("🧹 CLEAR ALL", self.clear_all, self.warning_color, self.button_fg)
        ]
        
        for text, command, bg_color, fg_color in file_buttons:
            btn = tk.Button(parent, text=text, command=command,
                          bg=bg_color, fg=fg_color, 
                          font=("Arial", 10, "bold"),
                          height=2, width=15, 
                          relief='raised', bd=3,
                          activebackground=self.highlight_color,
                          activeforeground=fg_color)
            btn.pack(side='left', padx=5, pady=5)

    def create_playback_controls(self, parent):
        """Create playback control buttons with theme colors"""
        control_buttons = [
            ("⏪ JUMP START", self.jump_top, self.button_bg, self.button_fg),
            ("◀ PREV SENTENCE", self.previous_sentence, self.accent_color, self.button_fg),
            ("▶ START AI", self.start_scroll, self.success_color, self.button_fg),
            ("⏸ PAUSE AI", self.toggle_scroll, self.highlight_color, '#000000'),
            ("⏹ STOP AI", self.stop_scroll, self.warning_color, self.button_fg),
            ("▶ NEXT SENTENCE", self.next_sentence, self.accent_color, self.button_fg),
            ("⏩ JUMP END", self.jump_bottom, self.button_bg, self.button_fg)
        ]
        
        for text, command, bg_color, fg_color in control_buttons:
            btn = tk.Button(parent, text=text, command=command, 
                          bg=bg_color, fg=fg_color,
                          font=("Arial", 9, "bold"), 
                          height=2, width=14, 
                          relief='raised', bd=2,
                          activebackground=self.highlight_color,
                          activeforeground=fg_color)
            btn.pack(side='left', padx=2, pady=2)

    def create_ai_features(self, parent):
        """Create AI feature controls with theme colors"""
        # Mode Selection
        mode_frame = tk.Frame(parent, bg=self.ui_bg_color)
        mode_frame.pack(fill='x', pady=5)
        
        tk.Label(mode_frame, text="AI Mode:", 
                fg=self.text_color, bg=self.ui_bg_color,
                font=("Arial", 10, "bold")).pack(side='left', padx=5)
        
        modes = ["AI Adaptive", "Sentence Highlight", "Word Highlight", "Speed Reading", "Rehearsal"]
        mode_combo = ttk.Combobox(mode_frame, textvariable=self.mode, values=modes,
                                 state="readonly", 
                                 font=("Arial", 10), 
                                 width=15,
                                 background=self.ui_bg_color,
                                 foreground=self.text_color)
        mode_combo.pack(side='left', padx=5)
        mode_combo.bind('<<ComboboxSelected>>', self.on_ai_mode_change)
        
        # Translation Controls
        trans_frame = tk.Frame(parent, bg=self.ui_bg_color)
        trans_frame.pack(fill='x', pady=10)
        
        tk.Label(trans_frame, text="Translate to:", 
                fg=self.text_color, bg=self.ui_bg_color,
                font=("Arial", 10, "bold")).pack(side='left', padx=5)
        
        # Language selection
        lang_values = [f"{code} - {name}" for code, name in self.languages.items()]
        self.lang_combo = ttk.Combobox(trans_frame, textvariable=self.target_language, 
                                      values=lang_values, state="readonly", 
                                      font=("Arial", 10), width=15,
                                      background=self.ui_bg_color,
                                      foreground=self.text_color)
        self.lang_combo.set("es - Spanish")
        self.lang_combo.pack(side='left', padx=5)
        
        # Translation button
        trans_btn = tk.Button(trans_frame, text="🌐 TRANSLATE", command=self.translate_content,
                            bg=self.info_color, fg=self.button_fg, 
                            font=("Arial", 9, "bold"),
                            height=1, width=12, 
                            relief='raised', bd=2,
                            activebackground=self.highlight_color)
        trans_btn.pack(side='left', padx=5)
        
        # Toggle translation display
        toggle_btn = tk.Button(trans_frame, text="👁 TOGGLE VIEW", command=self.toggle_translation_view,
                             bg=self.accent_color, fg=self.button_fg, 
                             font=("Arial", 9, "bold"),
                             height=1, width=12, 
                             relief='raised', bd=2,
                             activebackground=self.highlight_color)
        toggle_btn.pack(side='left', padx=5)
        
        # Feature Toggles
        toggles_frame = tk.Frame(parent, bg=self.ui_bg_color)
        toggles_frame.pack(fill='x', pady=10)
        
        features = [
            ("🤖 AI Adaptive Speed", self.ai_adaptive_speed),
            ("🎯 Auto-Pause", self.auto_pause),
            ("🪞 Mirror Mode", self.mirror_mode),
            ("👁 Eye Tracking Sim", self.eye_tracking_sim)
        ]
        
        for text, var in features:
            cb = tk.Checkbutton(toggles_frame, text=text, variable=var,
                              bg=self.ui_bg_color, fg=self.text_color, 
                              selectcolor=self.ui_bg_color,
                              activebackground=self.ui_bg_color,
                              activeforeground=self.text_color,
                              font=("Arial", 9), anchor='w')
            cb.pack(side='left', padx=10)

    def create_quick_settings(self, parent):
        """Create quick settings controls with theme colors"""
        # Speed Control
        speed_frame = tk.Frame(parent, bg=self.ui_bg_color)
        speed_frame.pack(fill='x', pady=5)
        
        tk.Label(speed_frame, text="Scroll Speed:", 
                fg=self.text_color, bg=self.ui_bg_color,
                font=("Arial", 9)).pack(side='left', padx=5)
        
        speed_scale = tk.Scale(speed_frame, from_=1, to=100, orient='horizontal',  # Wider range
                              variable=self.scroll_delay, showvalue=False,
                              length=300,  # Longer scale
                              bg=self.ui_bg_color, 
                              fg=self.text_color,
                              highlightbackground=self.ui_bg_color, 
                              troughcolor='#333333',
                              activebackground=self.highlight_color)
        speed_scale.pack(side='left', padx=5)
        speed_scale.bind('<Motion>', self.on_speed_change)
        
        self.speed_value_label = tk.Label(speed_frame, text=f"{self.scroll_delay.get()}ms",
                                         fg=self.highlight_color, 
                                         bg=self.ui_bg_color, 
                                         font=("Arial", 9, "bold"))
        self.speed_value_label.pack(side='left', padx=5)
        
        # Font Size Control
        size_frame = tk.Frame(parent, bg=self.ui_bg_color)
        size_frame.pack(fill='x', pady=5)
        
        tk.Label(size_frame, text="Font Size:", 
                fg=self.text_color, bg=self.ui_bg_color,
                font=("Arial", 9)).pack(side='left', padx=5)
        
        size_scale = tk.Scale(size_frame, from_=10, to=120, orient='horizontal',  # Wider range
                             variable=self.font_size, showvalue=False,
                             length=300,  # Longer scale
                             bg=self.ui_bg_color, 
                             fg=self.text_color,
                             highlightbackground=self.ui_bg_color, 
                             troughcolor='#333333',
                             activebackground=self.highlight_color)
        size_scale.pack(side='left', padx=5)
        size_scale.bind('<Motion>', self.on_font_size_change)
        
        self.size_value_label = tk.Label(size_frame, text=f"{self.font_size.get()}px",
                                        fg=self.highlight_color, 
                                        bg=self.ui_bg_color, 
                                        font=("Arial", 9, "bold"))
        self.size_value_label.pack(side='left', padx=5)

    def setup_ai_analytics_dashboard(self):
        """Setup the AI analytics dashboard with theme colors"""
        # Header
        header = tk.Frame(self.analytics_frame, bg=self.ui_bg_color, height=60)
        header.pack(fill='x', padx=10, pady=5)
        
        tk.Label(header, text="📊 AI PERFORMANCE DASHBOARD", 
                font=("Arial", 18, "bold"), 
                fg=self.text_color, 
                bg=self.ui_bg_color).pack(pady=15)
        
        # Main content
        content = tk.Frame(self.analytics_frame, bg=self.bg_color)
        content.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Performance metrics cards
        self.create_metrics_cards(content)
        
        # Session history
        self.create_session_history(content)
        
        # Controls
        self.create_analytics_controls(content)

    def create_metrics_cards(self, parent):
        """Create performance metric cards with theme colors"""
        cards_frame = tk.Frame(parent, bg=self.bg_color)
        cards_frame.pack(fill='x', pady=10)
        
        metrics = [
            ("⚡ AVERAGE WPM", "0", self.text_color),
            ("🎯 READING CONSISTENCY", "0%", self.highlight_color),
            ("🧠 FOCUS SCORE", "100%", self.accent_color),
            ("📈 IMPROVEMENT TREND", "+0%", self.info_color)
        ]
        
        self.metric_cards = []
        for i, (title, value, color) in enumerate(metrics):
            card = tk.Frame(cards_frame, 
                          bg=self.ui_bg_color, 
                          relief='raised', 
                          bd=2,
                          highlightbackground=self.border_color)
            card.pack(side='left', expand=True, fill='both', padx=5)
            
            tk.Label(card, text=title, font=("Arial", 10, "bold"), 
                    fg=color, bg=self.ui_bg_color).pack(pady=5)
            
            value_label = tk.Label(card, text=value, font=("Arial", 20, "bold"), 
                                 fg=color, bg=self.ui_bg_color)
            value_label.pack(pady=10)
            self.metric_cards.append(value_label)

    def create_session_history(self, parent):
        """Create session history display with theme colors"""
        history_frame = tk.LabelFrame(parent, text="📅 SESSION HISTORY", 
                                    fg=self.text_color, 
                                    bg=self.ui_bg_color, 
                                    font=("Arial", 12, "bold"), 
                                    padx=10, pady=10,
                                    highlightbackground=self.border_color)
        history_frame.pack(fill='both', expand=True, pady=10)
        
        self.history_text = scrolledtext.ScrolledText(history_frame, 
                                                     bg=self.canvas_bg, 
                                                     fg=self.text_color,
                                                     font=("Consolas", 9),
                                                     wrap=tk.WORD,
                                                     insertbackground=self.text_color,
                                                     selectbackground=self.highlight_color)
        self.history_text.pack(fill='both', expand=True, padx=5, pady=5)

    def create_analytics_controls(self, parent):
        """Create analytics control buttons with theme colors"""
        controls = tk.Frame(parent, bg=self.bg_color)
        controls.pack(fill='x', pady=10)
        
        control_buttons = [
            ("🔄 UPDATE DASHBOARD", self.update_dashboard, self.button_bg, self.button_fg),
            ("💾 EXPORT DATA", self.export_analytics, self.accent_color, self.button_fg),
            ("📊 GENERATE REPORT", self.generate_report, self.highlight_color, '#000000'),
            ("🧹 CLEAR DATA", self.clear_analytics, self.warning_color, self.button_fg)
        ]
        
        for text, command, bg_color, fg_color in control_buttons:
            btn = tk.Button(controls, text=text, command=command,
                          bg=bg_color, fg=fg_color, 
                          font=("Arial", 9, "bold"),
                          activebackground=self.highlight_color,
                          activeforeground=fg_color)
            btn.pack(side='left', padx=5, pady=5)

    def setup_ai_settings(self):
        """Setup AI settings panel with theme colors"""
        main_container = tk.Frame(self.settings_frame, bg=self.bg_color)
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Left column - Display settings
        left_col = tk.Frame(main_container, bg=self.bg_color)
        left_col.pack(side='left', fill='both', expand=True, padx=10)
        
        self.create_display_settings(left_col)
        self.create_audio_settings(left_col)
        
        # Right column - AI features
        right_col = tk.Frame(main_container, bg=self.bg_color)
        right_col.pack(side='right', fill='both', expand=True, padx=10)
        
        self.create_ai_feature_settings(right_col)
        self.create_theme_selector(right_col)

    def create_display_settings(self, parent):
        """Create display settings section with theme colors"""
        display_frame = tk.LabelFrame(parent, text="🖥 DISPLAY SETTINGS", 
                                    fg=self.text_color, 
                                    bg=self.ui_bg_color,
                                    font=("Arial", 12, "bold"), 
                                    padx=10, pady=10,
                                    highlightbackground=self.border_color)
        display_frame.pack(fill='x', pady=10)
        
        # Font size control
        size_control = tk.Frame(display_frame, bg=self.ui_bg_color)
        size_control.pack(fill='x', pady=5)
        
        tk.Label(size_control, text="Text Size:", 
                fg=self.text_color, bg=self.ui_bg_color,
                font=("Arial", 10)).pack(side='left')
        
        size_scale = tk.Scale(size_control, from_=10, to=120, orient='horizontal',  # Wider range
                             variable=self.font_size, showvalue=False,
                             length=300,  # Longer scale
                             bg=self.ui_bg_color, 
                             fg=self.text_color,
                             highlightbackground=self.ui_bg_color, 
                             troughcolor='#333333',
                             activebackground=self.highlight_color)
        size_scale.pack(side='left', padx=10)
        size_scale.bind('<Motion>', self.on_font_size_change)
        
        self.size_value_label = tk.Label(size_control, text=f"{self.font_size.get()}px",
                                        fg=self.highlight_color, 
                                        bg=self.ui_bg_color, 
                                        font=("Arial", 10, "bold"))
        self.size_value_label.pack(side='left', padx=10)
        
        # Speed control
        speed_control = tk.Frame(display_frame, bg=self.ui_bg_color)
        speed_control.pack(fill='x', pady=5)
        
        tk.Label(speed_control, text="Scroll Speed:", 
                fg=self.text_color, bg=self.ui_bg_color,
                font=("Arial", 10)).pack(side='left')
        
        speed_scale = tk.Scale(speed_control, from_=1, to=100, orient='horizontal',  # Wider range
                              variable=self.scroll_delay, showvalue=False,
                              length=300,  # Longer scale
                              bg=self.ui_bg_color, 
                              fg=self.text_color,
                              highlightbackground=self.ui_bg_color, 
                              troughcolor='#333333',
                              activebackground=self.highlight_color)
        speed_scale.pack(side='left', padx=10)
        speed_scale.bind('<Motion>', self.on_speed_change)
        
        self.speed_value_label = tk.Label(speed_control, text=f"{self.scroll_delay.get()}ms",
                                         fg=self.highlight_color, 
                                         bg=self.ui_bg_color, 
                                         font=("Arial", 10, "bold"))
        self.speed_value_label.pack(side='left', padx=10)

    def create_audio_settings(self, parent):
        """Create audio settings section with theme colors"""
        audio_frame = tk.LabelFrame(parent, text="🔊 AUDIO SETTINGS", 
                                  fg=self.text_color, 
                                  bg=self.ui_bg_color,
                                  font=("Arial", 12, "bold"), 
                                  padx=10, pady=10,
                                  highlightbackground=self.border_color)
        audio_frame.pack(fill='x', pady=10)
        
        if TTS_AVAILABLE:
            tk.Button(audio_frame, text="🔊 TEST SPEECH", command=self.test_speech,
                     bg=self.button_bg, fg=self.button_fg, 
                     font=("Arial", 10),
                     activebackground=self.highlight_color).pack(pady=5)
        
        if self.voice_available:
            tk.Button(audio_frame, text="🎤 CALIBRATE MIC", command=self.calibrate_microphone,
                     bg=self.accent_color, fg=self.button_fg, 
                     font=("Arial", 10),
                     activebackground=self.highlight_color).pack(pady=5)

    def create_ai_feature_settings(self, parent):
        """Create AI feature settings with theme colors"""
        ai_frame = tk.LabelFrame(parent, text="🤖 AI FEATURES", 
                               fg=self.text_color, 
                               bg=self.ui_bg_color,
                               font=("Arial", 12, "bold"), 
                               padx=10, pady=10,
                               highlightbackground=self.border_color)
        ai_frame.pack(fill='x', pady=10)
        
        features = [
            ("🎯 Auto-Pause at Sentences", self.auto_pause),
            ("👁 Eye Tracking Simulation", self.eye_tracking_sim),
            ("😊 Sentiment Analysis", self.sentiment_analysis),
            ("🎙 Voice Control", self.voice_control),
            ("🌐 Auto-Translation", self.show_translation)
        ]
        
        for text, var in features:
            cb = tk.Checkbutton(ai_frame, text=text, variable=var,
                              bg=self.ui_bg_color, 
                              fg=self.text_color, 
                              selectcolor=self.ui_bg_color,
                              activebackground=self.ui_bg_color,
                              activeforeground=self.text_color,
                              font=("Arial", 10), anchor='w')
            cb.pack(fill='x', pady=2)

    def create_theme_selector(self, parent):
        """Create theme selection with color preview"""
        theme_frame = tk.LabelFrame(parent, text="🎨 COLOR THEMES", 
                                  fg=self.text_color, 
                                  bg=self.ui_bg_color,
                                  font=("Arial", 12, "bold"), 
                                  padx=10, pady=10,
                                  highlightbackground=self.border_color)
        theme_frame.pack(fill='x', pady=10)
        
        # Create theme buttons with color preview
        themes_grid = tk.Frame(theme_frame, bg=self.ui_bg_color)
        themes_grid.pack(fill='x')
        
        themes = [
            ("🌙 Matrix", "matrix", "#00ff00"),
            ("🔵 Cyber", "cyber", "#00ffff"),
            ("🌅 Sunset", "sunset", "#ff6b6b"),
            ("🌊 Ocean", "ocean", "#4ecdc4"),
            ("🌳 Forest", "forest", "#6bcf7f"),
            ("🔥 Fire", "fire", "#ff6b6b"),
            ("🌌 Galaxy", "galaxy", "#9d4edd"),
            ("💡 Neon", "neon", "#ff00ff"),
            ("💰 Gold", "gold", "#ffd700"),
            ("❄️ Ice", "ice", "#e0f7ff")
        ]
        
        row = 0
        col = 0
        for text, theme_key, color in themes:
            btn_frame = tk.Frame(themes_grid, bg=self.ui_bg_color)
            btn_frame.grid(row=row, column=col, padx=5, pady=5)
            
            # Color preview
            color_preview = tk.Frame(btn_frame, bg=color, width=20, height=20, relief='sunken', bd=1)
            color_preview.pack(side='left', padx=(0, 5))
            
            btn = tk.Button(btn_frame, text=text, 
                          command=lambda t=theme_key: self.apply_theme(t),
                          bg=self.ui_bg_color, 
                          fg=color, 
                          font=("Arial", 9),
                          width=10, 
                          relief='raised', 
                          bd=2,
                          activebackground=self.highlight_color)
            btn.pack(side='left')
            
            col += 1
            if col > 3:
                col = 0
                row += 1

    # 🎨 COMPREHENSIVE COLOR MANAGEMENT SYSTEM

    def apply_theme(self, theme_name):
        """Apply a complete color theme to all UI elements"""
        if theme_name in self.themes:
            self.current_theme = theme_name
            theme = self.themes[theme_name]
            
            # Update all color variables
            self.bg_color = theme["bg"]
            self.text_color = theme["text"]
            self.highlight_color = theme["highlight"]
            self.accent_color = theme["accent"]
            self.ui_bg_color = theme["ui_bg"]
            self.progress_color = theme["progress"]
            self.button_bg = theme["button_bg"]
            self.button_fg = theme["button_fg"]
            self.canvas_bg = theme["canvas_bg"]
            self.status_bg = theme["status_bg"]
            self.border_color = theme["border"]
            self.warning_color = theme["warning"]
            self.success_color = theme["success"]
            self.info_color = theme["info"]
            
            # Update the entire UI
            self.update_theme_colors()
            self.theme_label.config(text=f"🎨 {theme_name.upper()}", fg=self.accent_color)
            
            messagebox.showinfo("🎨 Theme Applied", 
                              f"{theme_name.upper()} theme activated!\n\n"
                              f"• Background: {self.bg_color}\n"
                              f"• Text: {self.text_color}\n"
                              f"• Accent: {self.accent_color}")

    def update_theme_colors(self):
        """Update all UI elements with current theme colors"""
        try:
            # Update root background
            self.root.configure(bg=self.bg_color)
            
            # Update notebook styling
            style = ttk.Style()
            style.configure('TNotebook', background=self.ui_bg_color)
            style.configure('TNotebook.Tab', 
                           background=self.ui_bg_color, 
                           foreground=self.text_color)
            style.map('TNotebook.Tab', 
                     background=[('selected', self.accent_color)],
                     foreground=[('selected', '#ffffff')])
            
            # Update progress bar
            style.configure("Custom.Horizontal.TProgressbar", 
                           background=self.progress_color,
                           troughcolor='#333333')
            
            # Update all frames and backgrounds
            self.update_widget_colors(self.main_frame)
            self.update_widget_colors(self.control_frame)
            self.update_widget_colors(self.analytics_frame)
            self.update_widget_colors(self.settings_frame)
            
            # Update canvas
            self.canvas.configure(bg=self.canvas_bg, highlightbackground=self.border_color)
            if self.translation_canvas.winfo_ismapped():
                self.translation_canvas.configure(bg=self.canvas_bg, highlightbackground=self.highlight_color)
            
            # Update text display
            self.update_font_display()
            
            # Update status labels with new colors
            self.status_label.configure(bg=self.ui_bg_color, fg=self.success_color)
            self.theme_label.configure(bg=self.ui_bg_color, fg=self.accent_color)
            self.timer_label.configure(bg=self.status_bg, fg=self.text_color)
            self.wpm_label.configure(bg=self.status_bg, fg=self.highlight_color)
            self.focus_label.configure(bg=self.status_bg, fg=self.accent_color)
            self.mode_label.configure(bg=self.status_bg, fg=self.text_color)
            self.file_label.configure(bg=self.status_bg, fg=self.highlight_color)
            self.translation_status.configure(bg=self.status_bg, fg=self.info_color)
            self.progress_text.configure(bg=self.status_bg, fg=self.info_color)
            self.speed_value_label.configure(bg=self.ui_bg_color, fg=self.highlight_color)
            self.size_value_label.configure(bg=self.ui_bg_color, fg=self.highlight_color)
            
            # Force refresh of all UI elements
            self.root.update_idletasks()
            
        except Exception as e:
            print(f"Theme update error: {e}")

    def update_widget_colors(self, widget):
        """Recursively update colors for all widgets in a container"""
        try:
            # Update the widget itself if it's a Frame or LabelFrame
            if isinstance(widget, (tk.Frame, tk.LabelFrame)):
                widget.configure(bg=self.ui_bg_color)
                if hasattr(widget, 'cget') and 'fg' in widget.keys():
                    widget.configure(fg=self.text_color)
                if hasattr(widget, 'cget') and 'highlightbackground' in widget.keys():
                    widget.configure(highlightbackground=self.border_color)
            
            # Update all children widgets
            for child in widget.winfo_children():
                self.update_widget_colors(child)
                
        except Exception as e:
            # Silently handle any widget update errors
            pass

    # 🌈 ENHANCED COLOR FEATURES

    def get_contrast_color(self, hex_color):
        """Get contrasting text color for a background color"""
        try:
            # Convert hex to RGB
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            # Calculate luminance
            luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255
            
            # Return black or white based on luminance
            return '#000000' if luminance > 0.5 else '#ffffff'
        except:
            return '#ffffff'

    def create_color_gradient(self, start_color, end_color, steps):
        """Create a color gradient between two colors"""
        try:
            start_rgb = tuple(int(start_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            end_rgb = tuple(int(end_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            
            gradient = []
            for i in range(steps):
                ratio = i / (steps - 1)
                r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
                g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
                b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
                gradient.append(f'#{r:02x}{g:02x}{b:02x}')
            
            return gradient
        except:
            return [start_color, end_color]

    # 🎯 COLOR-BASED STATUS INDICATORS

    def update_status_color(self, status_type, message):
        """Update status label with appropriate color"""
        color_map = {
            'ready': self.success_color,
            'warning': self.warning_color,
            'error': self.warning_color,
            'info': self.info_color,
            'processing': self.highlight_color,
            'success': self.success_color
        }
        
        color = color_map.get(status_type, self.text_color)
        self.status_label.config(text=message, fg=color)

    def highlight_current_word_color(self):
        """Apply color-based highlighting to current word"""
        if (self.sentence_index < len(self.word_list) and 
            self.word_index < len(self.word_list[self.sentence_index])):
            
            # Create highlighted text with color formatting
            highlighted_text = ""
            for i, sentence_words in enumerate(self.word_list):
                for j, word in enumerate(sentence_words):
                    if i == self.sentence_index and j == self.word_index:
                        highlighted_text += f"[{word}] "
                    else:
                        highlighted_text += word + " "
                highlighted_text += " "
            
            if self.mirror_mode.get():
                highlighted_text = self.mirror_text(highlighted_text)
            
            self.canvas.itemconfig(self.text_id, text=highlighted_text.strip())

    # 🔧 FIXED AND ENHANCED METHODS

    def load_file(self):
        """Load a single file"""
        file_path = filedialog.askopenfilename(
            title="Select Script File",
            filetypes=[
                ("Text files", "*.txt"),
                ("Word documents", "*.docx"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.files = [file_path]
            self.current_file_index = 0
            self.process_file_content(file_path)
            self.file_label.config(text=f"📁 {os.path.basename(file_path)}")
            self.update_status_color('success', f"✅ LOADED: {os.path.basename(file_path)}")

    def load_multiple_files(self):
        """Load multiple files for sequential display"""
        file_paths = filedialog.askopenfilenames(
            title="Select Multiple Script Files",
            filetypes=[
                ("Text files", "*.txt"),
                ("Word documents", "*.docx"),
                ("All files", "*.*")
            ]
        )
        
        if file_paths:
            self.files = list(file_paths)
            self.current_file_index = 0
            self.process_file_content(self.files[0])
            
            file_names = [os.path.basename(f) for f in self.files]
            self.file_label.config(text=f"📁 {len(self.files)} files: {file_names[0]}...")
            self.update_status_color('success', f"✅ LOADED {len(self.files)} FILES")
            
            # Show next file button if multiple files
            if len(self.files) > 1:
                self.show_next_file_button()

    def show_next_file_button(self):
        """Show button to navigate to next file"""
        if hasattr(self, 'next_file_btn'):
            self.next_file_btn.destroy()
            
        self.next_file_btn = tk.Button(self.control_frame, 
                                     text=f"➡ NEXT FILE ({self.current_file_index + 1}/{len(self.files)})", 
                                     command=self.next_file,
                                     bg=self.accent_color, fg=self.button_fg,
                                     font=("Arial", 9, "bold"))
        # Find the file section and add button
        for widget in self.control_frame.winfo_children():
            if isinstance(widget, tk.LabelFrame) and "FILE MANAGER" in widget.cget('text'):
                self.next_file_btn.pack(in_=widget, side='left', padx=5, pady=5)
                break

    def next_file(self):
        """Load next file in sequence"""
        if self.files and len(self.files) > 1:
            self.current_file_index = (self.current_file_index + 1) % len(self.files)
            self.process_file_content(self.files[self.current_file_index])
            self.file_label.config(text=f"📁 {os.path.basename(self.files[self.current_file_index])} ({self.current_file_index + 1}/{len(self.files)})")
            self.update_status_color('info', f"📖 NOW READING: {os.path.basename(self.files[self.current_file_index])}")
            self.show_next_file_button()

    def process_file_content(self, file_path):
        """Process content from file"""
        try:
            content = ""
            if file_path.endswith('.docx') and DOCX_AVAILABLE:
                doc = Document(file_path)
                content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            else:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            
            self.text_content = content
            self.original_content = content
            self.process_ai_content()
            self.update_font_display()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def translate_content(self):
        """Translate content with synchronized scrolling"""
        if not TRANSLATION_AVAILABLE:
            messagebox.showinfo("Translation", 
                               "🌐 AI Translation requires: pip install deep-translator")
            return
        
        if not self.text_content.strip():
            messagebox.showwarning("Translation", "Please load content first")
            return
        
        self.is_translating = True
        self.translation_active = True
        self.update_status_color('processing', "🔄 TRANSLATING...")
        self.translation_status.config(text="🌐 Translating...", fg=self.highlight_color)
        
        # Show translation canvas with theme colors
        self.translation_canvas.pack(side='right', fill='both', expand=True, padx=(2, 0))
        self.translation_canvas.configure(bg=self.canvas_bg, highlightbackground=self.highlight_color)
        
        # Add translation canvas label
        self.canvas_label_right = tk.Label(self.translation_canvas, text="TRANSLATED TEXT", 
                                    bg=self.canvas_bg, fg=self.highlight_color,
                                    font=("Arial", 10, "bold"))
        self.canvas_label_right.place(x=50, y=10)
        
        # Start translation in thread
        threading.Thread(target=self.perform_translation, daemon=True).start()

    def perform_translation(self):
        """Perform translation in background thread"""
        try:
            target_lang = self.target_language.get().split(' - ')[0]
            translator = GoogleTranslator(source='auto', target=target_lang)
            
            # Split into sentences for better translation
            sentences = re.split(r'(?<=[.!?])\s+', self.text_content)
            translated_sentences = []
            
            for i, sentence in enumerate(sentences):
                if sentence.strip():
                    translated = translator.translate(sentence)
                    translated_sentences.append(translated)
                else:
                    translated_sentences.append("")
                
                # Update progress
                progress = (i + 1) / len(sentences) * 100
                self.root.after(0, lambda: self.update_translation_progress(progress))
            
            self.translated_content = ' '.join(translated_sentences)
            self.translated_sentences = translated_sentences
            
            # Process translated content for display
            self.root.after(0, self.finish_translation)
            
        except Exception as e:
            self.root.after(0, lambda: self.translation_error(str(e)))

    def finish_translation(self):
        """Finish translation setup"""
        self.is_translating = False
        self.update_status_color('success', "✅ TRANSLATION COMPLETE")
        self.translation_status.config(text="🌐 Translation: ON", fg=self.success_color)
        
        # Update translation display
        self.update_translation_display()
        messagebox.showinfo("Translation", "🌐 Translation completed successfully!")

    def translation_error(self, error):
        """Handle translation errors"""
        self.is_translating = False
        self.update_status_color('error', "❌ TRANSLATION FAILED")
        self.translation_status.config(text="🌐 Translation: ERROR", fg=self.warning_color)
        messagebox.showerror("Translation Error", f"Failed to translate: {error}")

    def update_translation_progress(self, progress):
        """Update translation progress"""
        self.translation_status.config(text=f"🌐 Translating... {int(progress)}%", fg=self.highlight_color)

    def update_translation_display(self):
        """Update translation canvas with translated text"""
        self.translation_canvas.delete("all")
        
        # Set up translation text
        font_size = self.font_size.get()
        font_style = (self.font_family, font_size)
        
        # Display full translated text
        self.translation_id = self.translation_canvas.create_text(
            self.translation_canvas.winfo_width() // 2,
            self.translation_canvas.winfo_height() // 2,
            text=self.translated_content,
            font=font_style,
            fill=self.text_color,
            width=self.translation_canvas.winfo_width() - 100,
            justify='center'
        )
        
        # Reset translation scroll position
        self.translation_y = 0

    def toggle_translation_view(self):
        """Toggle translation display on/off"""
        if self.translation_active and self.translated_content:
            if self.translation_canvas.winfo_ismapped():
                self.translation_canvas.pack_forget()
                self.translation_status.config(text="🌐 Translation: HIDDEN", fg=self.info_color)
            else:
                self.translation_canvas.pack(side='right', fill='both', expand=True, padx=(2, 0))
                self.translation_status.config(text="🌐 Translation: ON", fg=self.success_color)
        else:
            messagebox.showinfo("Translation", "Please translate content first")

    def start_scroll(self):
        """Start scrolling both original and translated text"""
        if not self.scrolling:
            self.scrolling = True
            self.session_start_time = time.time()
            self.update_status_color('processing', "▶ SCROLLING...")
            self.scroll_text()

    def stop_scroll(self):
        """Stop scrolling"""
        self.scrolling = False
        self.update_status_color('ready', "⏹ STOPPED")
        self.sentence_index = 0
        self.word_index = 0
        self.update_font_display()

    def toggle_scroll(self):
        """Toggle scrolling on/off"""
        if self.scrolling:
            self.scrolling = False
            self.update_status_color('info', "⏸ PAUSED")
        else:
            self.start_scroll()

    def scroll_text(self):
        """Scroll both original and translated text simultaneously"""
        if not self.scrolling:
            return
            
        # Scroll original text
        self.canvas.move(self.text_id, 0, -self.scroll_step.get())
        
        # Scroll translated text if active
        if self.translation_active and self.translation_canvas.winfo_ismapped():
            self.translation_canvas.move(self.translation_id, 0, -self.scroll_step.get())
        
        # Check if text has scrolled out of view
        bbox = self.canvas.bbox(self.text_id)
        if bbox and bbox[3] < 0:
            self.sentence_index += 1
            if self.sentence_index >= len(self.text_sentences):
                self.sentence_index = 0  # Loop back to beginning
                if self.files and len(self.files) > 1:
                    self.root.after(1000, self.next_file)  # Auto-advance to next file after delay
            
            self.word_index = 0
            self.update_font_display()
            self.reset_scroll_position()
        
        # Continue scrolling
        if self.scrolling:
            self.root.after(self.scroll_delay.get(), self.scroll_text)

    def reset_scroll_position(self):
        """Reset scroll position to top"""
        self.canvas.coords(self.text_id, self.canvas.winfo_width() // 2, 
                          self.canvas.winfo_height() + self.font_size.get())
        
        if self.translation_active and self.translation_canvas.winfo_ismapped():
            self.translation_canvas.coords(self.translation_id, 
                                          self.translation_canvas.winfo_width() // 2,
                                          self.translation_canvas.winfo_height() + self.font_size.get())

    def update_font_display(self):
        """Update font display for both canvases"""
        self.canvas.delete("all")
        
        # Display current sentence
        if self.text_sentences and self.sentence_index < len(self.text_sentences):
            current_sentence = self.text_sentences[self.sentence_index]
            
            font_size = self.font_size.get()
            font_style = (self.font_family, font_size)
            
            self.text_id = self.canvas.create_text(
                self.canvas.winfo_width() // 2,
                self.canvas.winfo_height() // 2,
                text=current_sentence,
                font=font_style,
                fill=self.text_color,
                width=self.canvas.winfo_width() - 100,
                justify='center'
            )
        
        # Update translation display if active
        if self.translation_active and self.translated_sentences and self.sentence_index < len(self.translated_sentences):
            self.translation_canvas.delete("all")
            
            current_translation = self.translated_sentences[self.sentence_index]
            
            font_size = self.font_size.get()
            font_style = (self.font_family, font_size)
            
            self.translation_id = self.translation_canvas.create_text(
                self.translation_canvas.winfo_width() // 2,
                self.translation_canvas.winfo_height() // 2,
                text=current_translation,
                font=font_style,
                fill=self.text_color,
                width=self.translation_canvas.winfo_width() - 100,
                justify='center'
            )

    def process_ai_content(self):
        """Process content for display"""
        # Split into sentences
        self.text_sentences = re.split(r'(?<=[.!?])\s+', self.text_content)
        self.word_list = [sentence.split() for sentence in self.text_sentences]
        
        # Reset position
        self.sentence_index = 0
        self.word_index = 0
        
        # Update display
        self.update_font_display()

    def on_font_size_change(self, event=None):
        """Handle font size change"""
        self.size_value_label.config(text=f"{self.font_size.get()}px")
        self.update_font_display()

    def on_speed_change(self, event=None):
        """Handle speed change"""
        self.speed_value_label.config(text=f"{self.scroll_delay.get()}ms")

    def on_ai_mode_change(self, event=None):
        """Handle AI mode change"""
        self.mode_label.config(text=f"🤖 {self.mode.get()}")

    def jump_top(self):
        """Jump to top"""
        self.sentence_index = 0
        self.word_index = 0
        self.update_font_display()
        self.reset_scroll_position()

    def jump_bottom(self):
        """Jump to bottom"""
        self.sentence_index = max(0, len(self.text_sentences) - 1)
        self.word_index = 0
        self.update_font_display()
        self.reset_scroll_position()

    def next_sentence(self):
        """Next sentence"""
        if self.text_sentences:
            self.sentence_index = (self.sentence_index + 1) % len(self.text_sentences)
            self.word_index = 0
            self.update_font_display()
            self.reset_scroll_position()

    def previous_sentence(self):
        """Previous sentence"""
        if self.text_sentences:
            self.sentence_index = (self.sentence_index - 1) % len(self.text_sentences)
            self.word_index = 0
            self.update_font_display()
            self.reset_scroll_position()

    def mirror_text(self, text):
        """Mirror text for teleprompter"""
        return text[::-1]

    # Placeholder methods for unimplemented features
    def save_script(self):
        messagebox.showinfo("Save", "Save functionality to be implemented")

    def new_script(self):
        self.text_content = "Enter your new script here..."
        self.process_ai_content()
        self.update_status_color('info', "📝 NEW SCRIPT CREATED")

    def clear_all(self):
        self.text_content = ""
        self.translated_content = ""
        self.files = []
        self.process_ai_content()
        self.update_status_color('warning', "🧹 ALL CLEARED")

    def test_speech(self):
        messagebox.showinfo("Speech", "Text-to-speech to be implemented")

    def calibrate_microphone(self):
        messagebox.showinfo("Microphone", "Microphone calibration to be implemented")

    def update_dashboard(self):
        messagebox.showinfo("Dashboard", "Dashboard update to be implemented")

    def export_analytics(self):
        messagebox.showinfo("Export", "Export functionality to be implemented")

    def generate_report(self):
        messagebox.showinfo("Report", "Report generation to be implemented")

    def clear_analytics(self):
        messagebox.showinfo("Clear", "Clear analytics to be implemented")

    def load_ai_config(self):
        """Load AI configuration"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    # Load configuration here
        except:
            pass

    def save_ai_config(self):
        """Save AI configuration"""
        try:
            config = {
                'theme': self.current_theme,
                'scroll_delay': self.scroll_delay.get(),
                'font_size': self.font_size.get()
            }
            with open(self.config_file, 'w') as f:
                json.dump(config, f)
        except:
            pass

    def setup_ai_keyboard_shortcuts(self):
        """Setup keyboard shortcuts"""
        self.root.bind('<F1>', lambda e: messagebox.showinfo("Help", "Keyboard shortcuts:\n\nSpace: Play/Pause\nLeft: Previous\nRight: Next\nF8: Translate"))
        self.root.bind('<F8>', lambda e: self.translate_content())
        self.root.bind('<space>', lambda e: self.toggle_scroll())
        self.root.bind('<Left>', lambda e: self.previous_sentence())
        self.root.bind('<Right>', lambda e: self.next_sentence())

    def start_ai_background_services(self):
        """Start background services"""
        # Start timer update
        self.update_timer()

    def update_timer(self):
        """Update session timer"""
        if self.session_start_time and self.scrolling:
            elapsed = time.time() - self.session_start_time
            hours = int(elapsed // 3600)
            minutes = int((elapsed % 3600) // 60)
            seconds = int(elapsed % 60)
            self.timer_label.config(text=f"🕒 {hours:02d}:{minutes:02d}:{seconds:02d}")
        
        self.root.after(1000, self.update_timer)

# 🚀 LAUNCH THE COLOR-ENHANCED AI TELEPROMPTER
if __name__ == "__main__":
    try:
        print("🎨🚀 Initializing Ultimate AI Teleprompter 4000 - Color Edition...")
        print("🌈 Loading 10 vibrant color themes...")
        
        root = tk.Tk()
        root.title("🎨🚀 ULTIMATE AI TELEPROMPTER 4000 - COLOR EDITION")
        
        app = UltimateAITeleprompter(root)
        
        print("✅ AI Teleprompter initialized successfully!")
        print("🎨 Color system activated with 10 themes")
        print("💡 Press F1 for help and press F8 for translation")
        
        # Show installation status with colors
        if not DOCX_AVAILABLE:
            print("📄 Word document support: NOT INSTALLED (pip install python-docx)")
        else:
            print("📄 Word document support: ✅ AVAILABLE")
            
        if not TRANSLATION_AVAILABLE:
            print("🌐 Translation support: NOT INSTALLED (pip install deep-translator)")
        else:
            print("🌐 Translation support: ✅ AVAILABLE")
            
        if not TTS_AVAILABLE:
            print("🔊 Text-to-speech: NOT INSTALLED (pip install gtts)")
        else:
            print("🔊 Text-to-speech: ✅ AVAILABLE")
        
        root.mainloop()
        
    except Exception as e:
        print(f"🚨 CRITICAL ERROR: {e}")
        messagebox.showerror("AI System Failure", 
                            f"Failed to initialize AI Teleprompter:\n\n{str(e)}\n\n"
                            "Please ensure all dependencies are properly installed.")