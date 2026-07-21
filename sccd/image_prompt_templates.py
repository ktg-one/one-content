"""
Awesome NotebookLM Image Prompt Templates Library
Derived from GitHub repository `notebooklm-prompt-styles` (YamilAyma/notebooklm-prompt-styles)
Provides curated YAML-inspired design tokens, visual archetypes, color palettes, and composition formulas.
"""

NOTEBOOKLM_PROMPT_STYLES = {
    "executive_report": {
        "theme": "Executive Report / Consulting",
        "style_guidelines": "Clean professional white background, deep blue accents, business-centric data visualization, executive presentation style",
        "color_palette": "Deep Navy (#051C2C), Muted Blue (#007DBB), Crisp White (#FFFFFF)",
        "composition": "Professional data-dense visual representation of {topic}, statement-driven grid, high information density, sharp contrast."
    },
    "emerald_corporate": {
        "theme": "Emerald Corporate High-Tech",
        "style_guidelines": "Deep emerald green with metallic silver accents, crystalline geometric shards, glassmorphic cards",
        "color_palette": "Deep Emerald (#0F3024), Metallic Silver (#C0C0C0), White (#FFFFFF)",
        "composition": "Executive high-tech visual of {topic}, sharp geometric shards, silver reflections, glassmorphic framing."
    },
    "silicon_refined": {
        "theme": "Silicon Refined Ultra-Minimalist",
        "style_guidelines": "Ultra-minimalist, premium tech aesthetic, generous whitespace, precision typography",
        "color_palette": "Matte Charcoal (#1D1D1F), Tech Blue (#0071E3), Pure White (#FFFFFF)",
        "composition": "Bento-style grid visual representing {topic}, airy composition, clean product-focused high fidelity rendering."
    },
    "liquid_executive": {
        "theme": "Liquid Executive Dark Mode",
        "style_guidelines": "Flowing blue liquid and smoke textures on solid black background, ultra-rounded containers",
        "color_palette": "Executive Blue (#0056B3), Pure Black (#000000), Surface Charcoal (#111111)",
        "composition": "Flowing blue liquid silk and smoke texture on solid black background illustrating {topic}, dramatic lighting, high contrast."
    },
    "clinical_precision": {
        "theme": "Clinical Precision High-Tech",
        "style_guidelines": "High-tech medical and scientific aesthetic, dark background contrast, royal blue glows",
        "color_palette": "Clinical Royal Blue (#2563EB), Pure Black (#000000), Slate Grey (#A1A1AA)",
        "composition": "Close-up schematic visualization of {topic}, soft royal blue light leak glow, clean minimalist linework."
    },
    "strategic_blue": {
        "theme": "Strategic Blue Tech-Forward",
        "style_guidelines": "Structured corporate design with light grey hexagonal geometric motifs and slate blue cards",
        "color_palette": "Slate Blue (#264653), Ice Blue (#E9F5F8), Slate Grey (#64748B)",
        "composition": "Tech-forward business illustration representing {topic}, hexagonal pattern overlay, crisp modern architectural grid."
    },
    "prestige_gold": {
        "theme": "Prestige Gold Dark Luxury",
        "style_guidelines": "Sophisticated gold-on-navy dark mode aesthetic with golden ethereal light curves",
        "color_palette": "Old Gold (#E2B670), Midnight Blue (#0F172A), Slate Surface (#1E293B)",
        "composition": "Ethereal golden hour lighting visual depicting {topic}, gold line accents, deep midnight blue background."
    },
    "cyber_ai": {
        "theme": "Cyber AI Futuristic",
        "style_guidelines": "Futuristic AI neural network aesthetic with glowing cybernetic linework and cyan lighting",
        "color_palette": "Cyber Cyan (#00F0FF), Neon Violet (#7B2CBF), Deep Space Black (#05050D)",
        "composition": "3D isometric neural network visual of {topic}, glowing data nodes, holographic interface, high-tech octane render."
    }
}

def build_awesome_prompt(topic, style_key="silicon_refined", focus_description=""):
    """
    Constructs an awesome image prompt pulling directly from GitHub notebooklm-prompt-styles.
    """
    tpl = NOTEBOOKLM_PROMPT_STYLES.get(style_key, NOTEBOOKLM_PROMPT_STYLES["silicon_refined"])
    
    prompt = (
        f"{focus_description or topic}. "
        f"Design Theme: {tpl['theme']}. "
        f"Style: {tpl['style_guidelines']}. "
        f"Color Palette: {tpl['color_palette']}. "
        f"Composition: {tpl['composition'].format(topic=topic)}."
    )
    return prompt

if __name__ == "__main__":
    print(build_awesome_prompt("AI Content Automation", style_key="silicon_refined"))
