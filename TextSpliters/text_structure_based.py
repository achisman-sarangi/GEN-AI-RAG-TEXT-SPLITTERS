from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """Artificial Intelligence (AI) is revolutionizing the healthcare industry, offering unprecedented opportunities to enhance patient care, streamline operations, and enable more accurate and timely decision-making. Through advanced algorithms and machine learning models, AI systems can analyze vast amounts of medical data, identify patterns, and predict potential health outcomes.

One of the most promising applications of AI in healthcare is in medical diagnostics. AI-powered tools can assist physicians by detecting anomalies in medical imaging, such as X-rays, CT scans, and MRIs, often with accuracy that rivals or surpasses human experts. These tools help reduce diagnostic errors and enable early detection of conditions such as cancer, heart disease, and neurological disorders.

In personalized medicine, AI is used to tailor treatments to individual patients based on their genetic makeup, lifestyle, and medical history. By analyzing complex datasets, AI can recommend optimal therapies and predict potential responses to different treatments, thereby improving efficacy and reducing side effects.

AI also enhances operational efficiency in healthcare settings. Automated systems can handle routine tasks like appointment scheduling, billing, and patient record management, freeing up healthcare professionals to focus on direct patient care. Additionally, AI-driven virtual assistants and chatbots are being used to provide basic health information, triage patient concerns, and facilitate telemedicine consultations.

However, the integration of AI in healthcare raises important considerations around data privacy, security, and ethical use. Ensuring that AI systems are transparent, unbiased, and respectful of patient rights is essential for maintaining trust and delivering equitable healthcare.

As AI technologies continue to evolve, their potential to improve healthcare outcomes, reduce costs, and enhance the patient experience is immense. With careful implementation and oversight, AI promises to be a transformative force in the future of healthcare."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0
)

result = splitter.split_text(text)

print(len(result))