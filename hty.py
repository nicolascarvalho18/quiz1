def quiz():
  
    perguntas = {
        "Qual é a capital do Brasil?": ["1) São Paulo", "2) Brasília", "3) Rio de Janeiro"],
        "Quem pintou a Mona Lisa?": ["1) Van Gogh", "2) Da Vinci", "3) Picasso"],
        "Qual é a fórmula da água?": ["1) CO2", "2) H2O", "3) O2"]
    }

    respostas_corretas = {
        "Qual é a capital do Brasil?": 2,
        "Quem pintou a Mona Lisa?": 2,
        "Qual é a fórmula da água?": 2
    }

    score = 0

    for pergunta, alternativas in perguntas.items():
        print(pergunta)
        for alternativa in alternativas:
            print(alternativa)
   
        resposta = int(input("Escolha a alternativa correta (1, 2, 3): "))
   
        if resposta == respostas_corretas[pergunta]:
            print("Resposta correta!")
            score += 1
        else:
            print("Resposta errada!")
        
        print()  

    print(f"Você acertou {score} de {len(perguntas)} perguntas!")


quiz()
