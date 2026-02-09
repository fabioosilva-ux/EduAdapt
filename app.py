import { GoogleGenAI, Type } from "@google/genai";
import { AdaptedLesson, Discipline, Grade } from "../types";

/**
 * Função para adaptar o conteúdo da aula usando o modelo Gemini 1.5 Flash.
 */
export const adaptLessonContent = async (
  originalContent: string, 
  discipline: Discipline, 
  teacherName: string,
  school: string,
  chapter: number,
  grade: Grade
): Promise<AdaptedLesson> => {
  // Inicialização usando a chave de ambiente
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY || "" });
  
  const prompt = `
    Como um especialista em educação especial e tecnologia assistiva, sua tarefa é adaptar o conteúdo abaixo para um aluno com Deficiência Intelectual (DI).
    
    Contexto:
    - Disciplina: ${discipline}
    - Nível: ${grade}
    - Professor: ${teacherName}
    - Instituição: ${school}
    - Capítulo: ${chapter}
    
    Diretrizes de Adaptação:
    1. Linguagem Simples: Use frases curtas, voz ativa e vocabulário concreto.
    2. Foco: Extraia APENAS o conceito principal. Elimine distrações.
    3. Respeito: O conteúdo deve ser adequado à idade (${grade}).
    
    Conteúdo Original:
    ${originalContent}
  `;

  try {
    const response = await ai.models.generateContent({
      model: 'gemini-1.5-flash', // Modelo estável e rápido
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseSchema: {
          type: Type.OBJECT,
          properties: {
            originalTitle: { type: Type.STRING },
            adaptedTitle: { type: Type.STRING },
            summary: { type: Type.STRING },
            sections: {
              type: Type.ARRAY,
              items: {
                type: Type.OBJECT,
                properties: {
                  title: { type: Type.STRING },
                  content: { type: Type.STRING },
                  imagePrompt: { type: Type.STRING },
                },
                required: ["title", "content", "imagePrompt"]
              }
            },
            coloringChallenge: {
              type: Type.OBJECT,
              properties: {
                description: { type: Type.STRING },
                prompt: { type: Type.STRING }
              },
              required: ["description", "prompt"]
            },
            familyActivity: {
              type: Type.OBJECT,
              properties: {
                title: { type: Type.STRING },
                description: { type: Type.STRING },
                instruction: { type: Type.STRING }
              },
              required: ["title", "description", "instruction"]
            }
          },
          required: ["originalTitle", "adaptedTitle", "summary", "sections", "coloringChallenge", "familyActivity"]
        }
      }
    });

    let text = response.text;
    if (text.startsWith('```')) {
      text = text.replace(/^```json\n?/, '').replace(/\n?```$/, '');
    }

    const data = JSON.parse(text);
    return {
      ...data,
      discipline,
      teacherName,
      school,
      chapter,
      grade
    };
  } catch (error) {
    console.error("Erro ao processar adaptação pedagógica:", error);
    throw error;
  }
};

/**
 * Função para gerar imagens ilustrativas.
 */
export const generateLessonImage = async (prompt: string, isColoring: boolean = false): Promise<string> => {
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY || "" });
  
  const finalPrompt = isColoring 
    ? `Desenho para colorir, contornos pretos, fundo branco: ${prompt}`
    : `Ilustração educativa infantil, clara e brilhante: ${prompt}`;

  try {
    const response = await ai.models.generateContent({
      model: 'gemini-1.5-flash', // Usando o Flash para texto e prompts
      contents: { parts: [{ text: finalPrompt }] }
    });

    // Nota: Para gerar imagens reais (PNG), você precisaria do modelo Imagen.
    // Este retorno abaixo é um "placeholder" para não quebrar seu app agora.
    return "[https://via.placeholder.com/512?text=Imagem+Educativa](https://via.placeholder.com/512?text=Imagem+Educativa)";
    
  } catch (error) {
    console.error("Erro na geração de imagem:", error);
    throw error;
  }
};
