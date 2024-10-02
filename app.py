import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import os
from PyPDF2 import PdfReader
# Import necessary LangChain components
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.embeddings import LocalEmbeddings

# Function to retrieve text from a selected PDF
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"  # Added newline for clarity
        except Exception as e:
            messagebox.showerror("Error", f"Error reading {pdf}: {e}")
    return text

# Function to handle PDF loading based on selections
def load_pdfs():
    folder_path = f"./pdfs/{selected_year.get()}/{selected_department.get()}/{selected_semester.get()}/{selected_subject.get()}"
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "No PDFs found for the selected options.")
        return None
    
    pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    if not pdf_files:
        messagebox.showerror("Error", "No PDFs found for the selected options.")
        return None

    # Extract and display the text from the PDFs
    pdf_text = get_pdf_text(pdf_files)
    if pdf_text:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Loaded PDFs: {len(pdf_files)} files loaded.\n", "system")
        chat_area.insert(tk.END, f"Text: {pdf_text[:500]}...\n", "system")  # Display a sample of the text
        chat_area.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Error", "Failed to load text from PDFs.")

# Function to handle manual PDF file selection
def select_pdf_files():
    file_paths = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        pdf_text = get_pdf_text(file_paths)
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Manually Loaded PDFs: {len(file_paths)} files loaded.\n", "system")
        chat_area.insert(tk.END, f"Text: {pdf_text[:500]}...\n", "system")  # Display a sample of the text
        chat_area.config(state=tk.DISABLED)

# Initialize the Ollama model and vector store
def initialize_ollama():
    global vector_store, ollama_model
    try:
        # Load your local Ollama model here
        ollama_model = Ollama(model="your_local_ollama_model_path")  # Replace with your actual model path
        embeddings = LocalEmbeddings(model="your_local_ollama_model_path")  # Replace with actual model path
        
        # Set up your vector store; ensure your FAISS index exists
        vector_store = FAISS.load_local("faiss_index", embeddings)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to initialize Ollama model: {e}")

# Function to handle the question submission
def submit_question():
    user_input = entry_box.get("1.0", 'end-1c').strip()
    if user_input:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {user_input}\n", "user")
        chat_area.insert(tk.END, "AI: Let me process that for you...\n", "ai")
        chat_area.config(state=tk.DISABLED)
        entry_box.delete("1.0", tk.END)
        
        try:
            # Perform similarity search in the vector store based on user input
            docs = vector_store.similarity_search(user_input)
            
            # Create a prompt template and process the question
            prompt = PromptTemplate(
                input_variables=["context", "question"],
                template="Context: {context}\nUser: {question}\nAI:"
            )
            chain = load_qa_chain(ollama_model, chain_type="stuff", verbose=True)
            
            # Generate a response
            ai_response = chain({"context": "\n".join(docs), "question": user_input})
            
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, f"AI: {ai_response['result']}\n", "ai")
            chat_area.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the question: {e}")
    else:
        messagebox.showwarning("Empty Input", "Please enter a question before submitting!")

# Create the main application window
window = tk.Tk()
window.title("Chat with PDF using Ollama AI")
window.geometry("600x700")
window.resizable(True, True)

# Set dark theme colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
highlight_color = "#0084ff"

# Model Selection at the Top
top_frame = tk.Frame(window, bg=bg_color)
top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

tk.Label(top_frame, text="Select Model:", font=("Arial", 12), bg=bg_color, fg=fg_color).pack(side=tk.LEFT, padx=5)
model_var = tk.StringVar(value="Ollama")
model_menu = ttk.Combobox(top_frame, textvariable=model_var, values=["Ollama"], state="readonly")
model_menu.pack(side=tk.LEFT, padx=5)

# Sidebar for selections
sidebar = tk.Frame(window, width=200, bg="#3a3a3a")
sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

# Dropdowns for year, department, semester, and subject
year_options = ["2020", "2021", "2022", "2023"]
department_options = ["CS", "IT", "ECE", "ME", "Civil"]
semester_options = ["1", "2", "3", "4", "5", "6", "7", "8"]
subject_options = ["Math", "Physics", "CS101", "Networks", "Algorithms"]

selected_year = tk.StringVar(value=year_options[0])
selected_department = tk.StringVar(value=department_options[0])
selected_semester = tk.StringVar(value=semester_options[0])
selected_subject = tk.StringVar(value=subject_options[0])

# Year dropdown
tk.Label(sidebar, text="Year", bg="#3a3a3a", fg=fg_color).pack(pady=5)
year_menu = ttk.Combobox(sidebar, textvariable=selected_year, values=year_options)
year_menu.pack(pady=5)

# Department dropdown
tk.Label(sidebar, text="Department", bg="#3a3a3a", fg=fg_color).pack(pady=5)
dept_menu = ttk.Combobox(sidebar, textvariable=selected_department, values=department_options)
dept_menu.pack(pady=5)

# Semester dropdown
tk.Label(sidebar, text="Semester", bg="#3a3a3a", fg=fg_color).pack(pady=5)
sem_menu = ttk.Combobox(sidebar, textvariable=selected_semester, values=semester_options)
sem_menu.pack(pady=5)

# Subject dropdown
tk.Label(sidebar, text="Subject", bg="#3a3a3a", fg=fg_color).pack(pady=5)
sub_menu = ttk.Combobox(sidebar, textvariable=selected_subject, values=subject_options)
sub_menu.pack(pady=5)

# Button to load PDFs
load_button = tk.Button(sidebar, text="Load PDFs", command=load_pdfs, bg=highlight_color, fg=fg_color)
load_button.pack(pady=10)

# Button to manually select PDFs
manual_load_button = tk.Button(sidebar, text="Select PDF Files", command=select_pdf_files, bg="#ffa500", fg=fg_color)
manual_load_button.pack(pady=10)

# Chat Area (ScrolledText)
chat_area_frame = tk.Frame(window, bg=bg_color)
chat_area_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

chat_area = scrolledtext.ScrolledText(chat_area_frame, wrap=tk.WORD, state=tk.DISABLED, bg="#1e1e1e", fg=fg_color)
chat_area.pack(fill=tk.BOTH, expand=True)
chat_area.tag_config("user", foreground=highlight_color, font=("Helvetica", 12, "bold"))
chat_area.tag_config("ai", foreground=fg_color, font=("Helvetica", 12))
chat_area.tag_config("system", foreground="#ff5733", font=("Helvetica", 12, "italic"))

# Entry box for user input
entry_frame = tk.Frame(window, bg=bg_color)
entry_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

entry_box = tk.Text(entry_frame, height=3, bg="#333333", fg=fg_color, wrap=tk.WORD)
entry_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Submit button
submit_button = tk.Button(entry_frame, text="Send", command=submit_question, bg=highlight_color, fg=fg_color)
submit_button.pack(side=tk.RIGHT)

# Initialize the Ollama model on startup
initialize_ollama()

# Run the main loop
window.mainloop()
