<h1><strong>
Avaliação de Robustez de Modelos TTS Multilíngue com
Dataset Multi-locutor de Diálogos em Português
</strong></h1>

<p>Material do Trabalho de Conclusão de Curso de Gustavo Wadas, no conexto  disponibilização pública de um novo dataset do projeto <a href="https://sites.google.com/view/tarsila-c4ai"><strong>TaRSila</strong></a></p> — o dataset 'Certas Palavras' —  para servir de treinamento para modelos de síntese de fala espontânea em Português Brasileiro.

<h2>Tabela de Áudios e Similaridades</h2>
<table border='1' cellspacing='0' cellpadding='4'>
<thead>
<tr>
<th rowspan='3'>ID</th>
<th colspan='3'>Transcrição</th>
</tr>
<tr>
<th>Ground Truth</th>
<th>YourTTS CP (CMLTTS Pre-Train)</th>
<th>F5TTS CP (CommonVoice Pre-Train)</th>
</tr>
<tr>
<th colspan='3'> Similaridades </th>
</tr>
<tr>
</thead>
<tbody>
<tr>
  <td rowspan='3'>01</td>
  <td colspan='3'><b>E eu gostaria de lembrar que um dos motivos da da realização dessa matéria se deve a um fato concreto, dentro de um plano moral, que foi, exatamente como a Bete acabou de falar, o Manifesto das Mulheres de Santana, no bairro daqui de São Paulo, e que teve uma eficácia teve uma eficácia na na no quadro social brasileiro, que foi ah que conseguiu mobilizar a nível de de primeiro escalão de governo, etecetera., mobilizar</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0038-CP015_950.037-979.634.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0038-CP015_950.037-979.634.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0038-CP015_950.037-979.634.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8502691388130188</center></td>
  <td><center>0.6984037160873413</center></td>
</tr>
<tr>
  <td rowspan='3'>02</td>
  <td colspan='3'><b>E voltamos ao Certas Palavras que conversa hoje com Marta Suplicy, que pela editora efe tê dê, lançou recentemente em praça pública, o livro Papai, Mamãe e Eu, aliás esse livro que trata da orientação e educação sexual eh está sendo oferecido hoje pela editora efe tê dê ao ouvinte do Certas Palavras, você pode ganhar esse livro e para e para isso você deve escrever para o programa Certas Palavras, põe na frente da carta programa</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0075-CP566_1103.39-1132.82.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0075-CP566_1103.39-1132.82.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0075-CP566_1103.39-1132.82.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9352328181266785</center></td>
  <td><center>0.7620540261268616</center></td>
</tr>
<tr>
  <td rowspan='3'>03</td>
  <td colspan='3'><b>Você daqui a pouco vai conhecer esse novo trabalho de Marta Suplicy. Na segunda parte do programa, ehh, nós vamos reapresentar, reapresentar, um trecho, uma edição da entrevista que realizamos ao vivo na quarta feira a tarde com Márcio Souza. Márcio Souza, ehh, escritor do Amazonas que lançou recentemente o livro</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0062-CP566_88.377-117.588.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0062-CP566_88.377-117.588.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0062-CP566_88.377-117.588.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9433948397636414</center></td>
  <td><center>0.8432798981666565</center></td>
</tr>
<tr>
  <td rowspan='3'>04</td>
  <td colspan='3'><b>avaliação em relação ao universo da criança, do adolescente, mais ou menos você já deu uma pista numa outra resposta sua aqui nessa conversa, mas ãh algumas informações assim mais precisas sobre exatamente a o universo contemporâneo, ãh, o universo atual dos adolescentes, crianças, que você pôde constatar a partir da edição dos seus livros, da resposta dessas crianças, desses adolescentes até você,</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0049-CP516_860.377-889.277.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0049-CP516_860.377-889.277.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0049-CP516_860.377-889.277.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9608429670333862</center></td>
  <td><center>0.7351904511451721</center></td>
</tr>
<tr>
  <td rowspan='3'>05</td>
  <td colspan='3'><b>do seguinte caráter, o liberalismo, ele é, digamos, uma, talvez entre aspas, uma doutrina ou eh um um leque de conceitos eh em progresso, ele te ele está, digamos eh, ele está resolvido enquanto a sua base teórica, ele é hoje um ele é um domínio já assentado ou ele, exatamente, ele até necessita de uma progressão teórica?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0051-CP574_1225.1-1253.97.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0051-CP574_1225.1-1253.97.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0051-CP574_1225.1-1253.97.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9545097351074219</center></td>
  <td><center>0.7580673694610596</center></td>
</tr>
<tr>
  <td rowspan='3'>06</td>
  <td colspan='3'><b>Com Certas Palavras, o programa de livros e ideias da cê bê ene Brasil, lembrando você que é professor você também de repente que você que é pai que tem dificuldade até no contato educacional do ponto de vista educacional, didático, formal com seus filhos, escreva para o Certas Palavras respondendo duas questõezinhas simples, quais são os assuntos que você gostaria de ver abordado aqui, abordados aqui no Certas Palavras, você que é professor e também</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0012-CP660_1028.2-1056.77.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0012-CP660_1028.2-1056.77.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0012-CP660_1028.2-1056.77.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.94040846824646</center></td>
  <td><center>0.8369693756103516</center></td>
</tr>
<tr>
  <td rowspan='3'>07</td>
  <td colspan='3'><b>Bom Sandra, você, agora, depois de, de toda essa, essa confusão, a gente pode chamar assim, você sai com o livro, O Flagrante da Farsa. Antes de contar a história, evidentemente é um livro que trata da história da Operação Uruguai, como é que foi revelado, o que aconteceu com você antes e depois, esse tipo de coisa. Eu quero te saber o seguinte, eh, como é que você se sente, ãh, assinando um livro. O que significa o livro para você...</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0006-CP553_199.428-227.778.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0006-CP553_199.428-227.778.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0006-CP553_199.428-227.778.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.936771810054779</center></td>
  <td><center>0.7299379110336304</center></td>
</tr>
<tr>
  <td rowspan='3'>08</td>
  <td colspan='3'><b>questões, ligada a censura e inclusive conseguiu, mesmo que digam em contrário, tirar um programa de televisão do ar, o que eh sem, digamos assim, eh julgar premeditadamente, é um fato grave, me parece que é um fato grave que uma atitude eh ih eh de cunho moral tenha conseguido,eh  dentro da rede de televisão mais poderosa do Brasil, quiçá né da América Latina, eh obter esse sucesso.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0039-CP015_979.92-1007.45.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0039-CP015_979.92-1007.45.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0039-CP015_979.92-1007.45.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8505388498306274</center></td>
  <td><center>0.7150815725326538</center></td>
</tr>
<tr>
  <td rowspan='3'>09</td>
  <td colspan='3'><b>Depois de Marta Suplicy, nós vamos ouvir novamente, vamos a reapresentar uma edição da entrevista que realizamos na última quarta-feira ao vivo, na tarde especial da Nova Eldorado á eme, com o escritor amazonense Márcio Souza, que pela editora Marco Zero acabou de lançar O Empate contra Chico Mendes, um livro que fala da Amazônia e das atividades sindical</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0002-CP566_32.147-59.247.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0002-CP566_32.147-59.247.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0002-CP566_32.147-59.247.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9113330841064453</center></td>
  <td><center>0.7378909587860107</center></td>
</tr>
<tr>
  <td rowspan='3'>10</td>
  <td colspan='3'><b>já apontamos aqui nessa entrevista, esse segmento eh infanto-juvenil, mas, principalmente, eu acho que os livros eh que se pretendem eh dedicados às crianças mais tenra-idade, eles proliferaram, foi um mercado que cresceu bastante e, numa certa medida, como eu creio que, historicamente, já é ah já já está carimbado, já está legitimado, que eh a revista Recreio foi</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0058-CP675_1024.93-1051.82.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0058-CP675_1024.93-1051.82.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0058-CP675_1024.93-1051.82.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9678797125816345</center></td>
  <td><center>0.5992069244384766</center></td>
</tr>
<tr>
  <td rowspan='3'>11</td>
  <td colspan='3'><b>Keila, eu gostaria de, antes da da de colocar a questão para você, de lembrar essa maravilha que é a contradição né do do nome da escrava que agora tem o nome do seu título e as circunstâncias de vida dela ser escrava, quer dizer, uma escrava chamada Liberata é algo que realmente chama atenção e quanto a questão propriamente dita, eu gostaria que você fizesse uma reflexão Keila</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0002-CP662_551.411-577.871.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0002-CP662_551.411-577.871.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0002-CP662_551.411-577.871.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9387568235397339</center></td>
  <td><center>0.759974479675293</center></td>
</tr>
<tr>
  <td rowspan='3'>12</td>
  <td colspan='3'><b>eh depois de de descontado todos os custos eh industriais é mais do que o o o dinheiro que a prefe a prefeitura de Manaus dispõe durante o ano todo para os seus programas e a e a JAF não paga nada ô Márcio, o trinta segundos nós estamos encerrando o programa eu queria saber de você o seguinte era possível Márcio Souza existir como conhecemos hoje Márcio Souza se vivesse até hoje em Manaus se não tivesse passado pelo Rio</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0054-CP658_1736.28-1762.56.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0054-CP658_1736.28-1762.56.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0054-CP658_1736.28-1762.56.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9508346319198608</center></td>
  <td><center>0.8279046416282654</center></td>
</tr>
<tr>
  <td rowspan='3'>13</td>
  <td colspan='3'><b>digamos, de ordem interna, num órgão como o IBGE, para vocês que são profissionais desse instituto, o que vocês mais comentam, por exemplo, quando vocês têm uma definição estatística dessas que estão contidas aqui nesse nesse exemplar, aquelas que vocês mais comentam, que são importantes para vocês mesmo, que vocês entendem que, sendo importantes para vocês, é importante para o país?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0029-CP558_715.473-739.705.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0029-CP558_715.473-739.705.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0029-CP558_715.473-739.705.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9557164907455444</center></td>
  <td><center>0.6203424334526062</center></td>
</tr>
<tr>
  <td rowspan='3'>14</td>
  <td colspan='3'><b>Cardoso Pires, eu queria saber de você o seguinte, já que a gente está falando tanto aí no no inconsciente, tocamos do lado do estilo, e você também falou da crítica e da crítica criativa, que revela coisas às vezes que você surpreende, eu gostaria de saber o seguinte, essa crítica já te mostrou um livro, o próprio público já te revelou um um livro seu?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0019-CP270_1654.75-1678.23.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0019-CP270_1654.75-1678.23.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0019-CP270_1654.75-1678.23.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.958821177482605</center></td>
  <td><center>0.7634027004241943</center></td>
</tr>
<tr>
  <td rowspan='3'>15</td>
  <td colspan='3'><b>Paulo, eh, todo mundo sabe Avenida Brasil, sexto da série, são, todo ano você lança em função do trabalho que você executa na revista Isto É. Explica tecnicamente, uma dessas questões técnicas primeiras, quer dizer, esse é o, é o apanhado desse ano de noventa e quatro, quais são os eventos que você retratou aqui nessa sua charge, nesse seu trabalho?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0010-CP657_150.993-172.725.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0010-CP657_150.993-172.725.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0010-CP657_150.993-172.725.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.95180344581604</center></td>
  <td><center>0.8102843761444092</center></td>
</tr>
<tr>
  <td rowspan='3'>16</td>
  <td colspan='3'><b>Você deve estar lembrado, realmente foi, teve uma cobertura muito grande, o assassinato do advogado Paulo Paulo Fonteles, em oitenta e sete, se não me engano, todos os jornais, todas as tê vês, eh falaram desse cli desse crime, uma vez que Paulo Fonteles era o mais importante advogado de posseiros e sem terras do norte do país, não Luiz?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0012-CP672_56.998-77.066.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0012-CP672_56.998-77.066.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0012-CP672_56.998-77.066.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9624974727630615</center></td>
  <td><center>0.8005068302154541</center></td>
</tr>
<tr>
  <td rowspan='3'>17</td>
  <td colspan='3'><b>Acabamos de fazer a entrevista com a Marilene Felinto e tal, citamos o caso do Luiz Roncari, que também é um, é um escritor forte que, e que já tem alguns livros lançados e que passou por toda uma dificuldade frente ao mercado editorial, frente ao mercado, né? Frente à própria escrita e tal.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0051-CP575_9.039-27.164.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0051-CP575_9.039-27.164.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0051-CP575_9.039-27.164.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9728101491928101</center></td>
  <td><center>0.7926024198532104</center></td>
</tr>
<tr>
  <td rowspan='3'>18</td>
  <td colspan='3'><b>Nós estamos terminando, mas só uma pergunta, já que o o o Jorge Mattoso tem uma uma visão internacional né da da questão do usuário no trabalho da parte dele, se esse tipo de comportamento é um comportamento eh brasileiro, terceiro mundista ou ou é um comportamento mundial?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0033-CP701_1441.43-1458.93.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0033-CP701_1441.43-1458.93.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0033-CP701_1441.43-1458.93.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9503316283226013</center></td>
  <td><center>0.7954185009002686</center></td>
</tr>
<tr>
  <td rowspan='3'>19</td>
  <td colspan='3'><b>Quer dizer, e o que significa para mim uma forte vontade de continuar vivendo, quer dizer, porque a mensagem, quer dizer, a linguagem ela persiste, né, a mensagem daquela pessoa, ela persiste. Não sei, até buscando uma imortalidade assim. É isso o que você encontrou também?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0002-CP574_515.377-532.05.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0002-CP574_515.377-532.05.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0002-CP574_515.377-532.05.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9421817660331726</center></td>
  <td><center>0.7946294546127319</center></td>
</tr>
<tr>
  <td rowspan='3'>20</td>
  <td colspan='3'><b>A apresentação, o o i bê gê é, o material eh editorial do i bê gê é, ele está com um perfil, de desse está dentro desse novo perfil do mercado editorial brasileiro, uma boa apresentação, eh um bom papel, a coisa é bonita realmente?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0044-CP558_1553.1-1569.43.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0044-CP558_1553.1-1569.43.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0044-CP558_1553.1-1569.43.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9484741687774658</center></td>
  <td><center>0.7921465635299683</center></td>
</tr>
<tr>
  <td rowspan='3'>21</td>
  <td colspan='3'><b>Veja bem, a questão da Segunda Guerra que começou lá, e depois a que a questão do comunismo, e parece, pelo que você conta, que a questão da religiosidade continua muito forte naquele país, e tem e com aspectos políticos, inclusive.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0036-CP546_628.616-643.728.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0036-CP546_628.616-643.728.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0036-CP546_628.616-643.728.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9446446895599365</center></td>
  <td><center>0.6901218295097351</center></td>
</tr>
<tr>
  <td rowspan='3'>22</td>
  <td colspan='3'><b>Isso porque nós ehconhecemos a a sua trajetória, né, profissional e, seguramente, que a última coisa que eu poderia que eu particularmente poderia imaginar é você um correspondente de guerra.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0016-CP655_570.568-585.559.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0016-CP655_570.568-585.559.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0016-CP655_570.568-585.559.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9025808572769165</center></td>
  <td><center>0.7000318765640259</center></td>
</tr>
<tr>
  <td rowspan='3'>23</td>
  <td colspan='3'><b>Cláudio, não sei o que eh eu e o o o Jorge, coincidência apenas, eh nos soa um pouco falso sempre quando se fala de que a grande revolução do final do século é a revolução da informática.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0026-CP723_629.04-643.998.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0026-CP723_629.04-643.998.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0026-CP723_629.04-643.998.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9521042108535767</center></td>
  <td><center>0.8942938446998596</center></td>
</tr>
<tr>
  <td rowspan='3'>24</td>
  <td colspan='3'><b>Trata-se exatamente do fato de que este ano, eh ano do centenário do futebol brasileiro, ano de Copa do Mundo, o Brasil é tema da Feira do Livro de Frankfurt, a mais importante feira do livro de todo o mundo.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0009-CP679_49.635-64.548.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0009-CP679_49.635-64.548.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0009-CP679_49.635-64.548.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9157766103744507</center></td>
  <td><center>0.6928492784500122</center></td>
</tr>
<tr>
  <td rowspan='3'>25</td>
  <td colspan='3'><b>Muito bem, agradecemos a presença aqui no Certas Palavras da escritora dramaturga Leilah Assumpção, que lança agora pela editora Cipione o texto da sua peça Lua Nua.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0041-CP513_813.117-828.029.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0041-CP513_813.117-828.029.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0041-CP513_813.117-828.029.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.948500394821167</center></td>
  <td><center>0.7107319831848145</center></td>
</tr>
<tr>
  <td rowspan='3'>26</td>
  <td colspan='3'><b>Agora, me diga um pouco, vamos falar um pouquinho eh desses temas, quer dizer, eh esse esse time de intelectuais que vocês organizaram, se foi eh já por predileções anteriores, que já tinham noção eh e textos anteriores sobre o futebol, ou não?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0037-CP656_685.911-700.805.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0037-CP656_685.911-700.805.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0037-CP656_685.911-700.805.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9629051089286804</center></td>
  <td><center>0.8453232049942017</center></td>
</tr>
<tr>
  <td rowspan='3'>27</td>
  <td colspan='3'><b>na fila. Agora, por exemplo, no caso, não de uma música, mas de um poema, sei lá, o certas palavras com o Lima Duarte, na poesia do do Carlos Dummond de Andrade, se ele quiser ouvir, não o disco inteiro, mas cinco, seis, sete vezes o mesmo poema, ele pode?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0083-CP520_1425.34-1440.2.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0083-CP520_1425.34-1440.2.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0083-CP520_1425.34-1440.2.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9467246532440186</center></td>
  <td><center>0.7653769254684448</center></td>
</tr>
<tr>
  <td rowspan='3'>28</td>
  <td colspan='3'><b>A Ivana que é jornalista, aliás, tem uma uma história de família dedicada ao livro, a o pai da Ivana, da Ivana Jinkings, tem a e a livraria Jinkings, que inclusive foi conside foi eleita a livraria do ano ano passado, né?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0022-CP716_125.057-139.862.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0022-CP716_125.057-139.862.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0022-CP716_125.057-139.862.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9367270469665527</center></td>
  <td><center>0.8297762274742126</center></td>
</tr>
<tr>
  <td rowspan='3'>29</td>
  <td colspan='3'><b>E também saber o seguinte, se a campanha é assim, quer dizer, se a a campanha, ela não pertence à política enquanto aquela política já funcionada, quer dizer, ou funcional, quer dizer, a política que está na na Assembleia ou que está em Brasília.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0020-CP646_886.995-901.781.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0020-CP646_886.995-901.781.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0020-CP646_886.995-901.781.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9456422328948975</center></td>
  <td><center>0.7216942310333252</center></td>
</tr>
<tr>
  <td rowspan='3'>30</td>
  <td colspan='3'><b>Então, o usuário, por exemplo, se ele não adquiriu uma pequena apostila num curso qualquer, ele vai ter que adquirir vários livros para poder estudar esta matéria ou o conteúdo programático necessário para o concurso público tá e.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0023-CP702_409.961-424.671.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0023-CP702_409.961-424.671.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0023-CP702_409.961-424.671.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9525278806686401</center></td>
  <td><center>0.8568604588508606</center></td>
</tr>
<tr>
  <td rowspan='3'>31</td>
  <td colspan='3'><b>E deixando eh também como uma referência que a Leila, a exemplo dos Mamonas né, que mais ou menos isso que você falou, não evidentemente com o contexto da Leila, também acabou morrendo num acidente eh de avião né, mas não no Brasil.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0021-CP743_198.693-213.324.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0021-CP743_198.693-213.324.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0021-CP743_198.693-213.324.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9352558851242065</center></td>
  <td><center>0.7826241850852966</center></td>
</tr>
<tr>
  <td rowspan='3'>32</td>
  <td colspan='3'><b>É. é que Veja bem, essa experiência, eu gostaria que você relatasse a experiência dele, que você torna importante no seu livro, e me dissesse o seguinte, esse pidinte, quer dizer, com quem a a ideia do religioso do Brasil, do beato no Brasil, é do pidinte.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0067-CP546_1576.56-1591.05.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0067-CP546_1576.56-1591.05.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0067-CP546_1576.56-1591.05.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9296450614929199</center></td>
  <td><center>0.701040506362915</center></td>
</tr>
<tr>
  <td rowspan='3'>33</td>
  <td colspan='3'><b>Começa agora mais uma edição do programa de livros e ideias da cê bê ene Brasil, Certas Palavras, que hoje vai contar com a presença da radialista, cineasta, ex-cineasta, você falou, Regina?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0002-CP674_14.303-28.709.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0002-CP674_14.303-28.709.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0002-CP674_14.303-28.709.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9543588161468506</center></td>
  <td><center>0.7295337915420532</center></td>
</tr>
<tr>
  <td rowspan='3'>34</td>
  <td colspan='3'><b>Você já deu ideia eh para o ouvinte no programa passado do do livro, gostaria que você falasse rapidamente e desse um exemplo, por exemplo, desse seu tra do desse seu trabalho com com um dos biografados.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0007-CP659_44.96-59.351.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0007-CP659_44.96-59.351.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0007-CP659_44.96-59.351.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8979786038398743</center></td>
  <td><center>0.800744354724884</center></td>
</tr>
<tr>
  <td rowspan='3'>35</td>
  <td colspan='3'><b>O Hélio Gaspar fez uma escreveu uma fez uma pequena entrevista com um jornalista americano em que ele falou, pô, isso é um caso sério, uma pessoa espancada no Central Park, quando no Parque do Ibirapuera você vai lá é todo dia, é uma pessoa espancada no Central Park.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0081-CP742_1205.92-1220.17.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0081-CP742_1205.92-1220.17.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0081-CP742_1205.92-1220.17.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9588403701782227</center></td>
  <td><center>0.8844454288482666</center></td>
</tr>
<tr>
  <td rowspan='3'>36</td>
  <td colspan='3'><b>entre eh esse essa geração que se apresenta, ficcionista, ou não alguma coisa que te chame a atenção, que tenha que tenha até sido útil para você, que tenha  sido um ponto que seja um ponto de referência importante?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0081-CP707_1445.36-1459.61.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0081-CP707_1445.36-1459.61.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0081-CP707_1445.36-1459.61.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9286596179008484</center></td>
  <td><center>0.8391385078430176</center></td>
</tr>
<tr>
  <td rowspan='3'>37</td>
  <td colspan='3'><b>Eu acho que eh ti eh há pouco tempo atrás, há poucos anos atrás, o problema do do debate político, no sentido mais amplo, no sentido mais macro e até nu num num se num sentido mais sofisticado, ele estava muito mais aberto do que hoje.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0035-CP515_538.25-552.437.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0035-CP515_538.25-552.437.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0035-CP515_538.25-552.437.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9457370042800903</center></td>
  <td><center>0.6585664749145508</center></td>
</tr>
<tr>
  <td rowspan='3'>38</td>
  <td colspan='3'><b>tratando ligeiramente pacientes, porque é é o caso, quer dizer, num não há possibilidade de de de ter, para uma massa imensa de miseráveis que nós temos, um tratamento mais adequado que aquilo.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0054-CP723_1393.72-1407.89.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0054-CP723_1393.72-1407.89.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0054-CP723_1393.72-1407.89.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9633811116218567</center></td>
  <td><center>0.916131317615509</center></td>
</tr>
<tr>
  <td rowspan='3'>39</td>
  <td colspan='3'><b>Como é que se muda, então, é o que a gente poderia chamar essa cultura política de saber que que o ehh que acabar com o Marajá, com um Marajá ou dois Marajás, não significa nada, porque outros virão.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0053-CP344_1820.6-1834.65.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0053-CP344_1820.6-1834.65.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0053-CP344_1820.6-1834.65.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9282575249671936</center></td>
  <td><center>0.7074477672576904</center></td>
</tr>
<tr>
  <td rowspan='3'>40</td>
  <td colspan='3'><b>um um dos órgãos da Fundação Biblioteca Nacional, Márcio Souza, que está no estúdio da cê bê ene Rio de Janeiro e que, pela editora Marco Zero, está saindo com mais um livro, A Caligrafia de Deus.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0006-CP658_109.983-123.966.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0006-CP658_109.983-123.966.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0006-CP658_109.983-123.966.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9252854585647583</center></td>
  <td><center>0.7428233623504639</center></td>
</tr>
<tr>
  <td rowspan='3'>41</td>
  <td colspan='3'><b>E só uma complementação, eu gostaria de saber, quer dizer, se atribui isso sempre aos militares, se os civis também não adotaram, alguns civis, com muito carinho, essa tática de de deixar o adversário de lado para torná-lo inimigo.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0020-CP514_575.103-589.031.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0020-CP514_575.103-589.031.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0020-CP514_575.103-589.031.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9568389058113098</center></td>
  <td><center>0.774775505065918</center></td>
</tr>
<tr>
  <td rowspan='3'>42</td>
  <td colspan='3'><b>e ideias, o Certas Palavras, que hoje, com muito prazer, recebe a carioca jornalista, escritora de dezenas de livros e está lançando mais quatro de uma vez para a sua coleção.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0007-CP675_22.374-36.285.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0007-CP675_22.374-36.285.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0007-CP675_22.374-36.285.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9446501731872559</center></td>
  <td><center>0.7288743257522583</center></td>
</tr>
<tr>
  <td rowspan='3'>43</td>
  <td colspan='3'><b>Você estava falando exatamente do declínio da chanchada, e eu lembro esse jota cá, a que você se refere aqui no subtítulo, a chanchada de Getúlio a jota cá, e jota cá foi um momento de grande explosão da indústria brasileira, né?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0039-CP511_1013.03-1026.81.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0039-CP511_1013.03-1026.81.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0039-CP511_1013.03-1026.81.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9035622477531433</center></td>
  <td><center>0.7640988826751709</center></td>
</tr>
<tr>
  <td rowspan='3'>44</td>
  <td colspan='3'><b>O professor eh Francisco Antônio Dória, convidado de hoje do Certas Palavras, autor do livro Os Herdeiros do Poder, um livro da editora Revan, que você quer conhecer um pouco sobre a estrutura de poder do Brasil.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0071-CP712_1406.73-1420.38.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0071-CP712_1406.73-1420.38.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0071-CP712_1406.73-1420.38.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9637956619262695</center></td>
  <td><center>0.8166584372520447</center></td>
</tr>
<tr>
  <td rowspan='3'>45</td>
  <td colspan='3'><b>O José Nogueira quer saber o seguinte Ney, como é que você vê essa questão da volta da censura, ou pelo menos se discutir a volta da censura no Brasil?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0026-CP627_997.575-1010.88.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0026-CP627_997.575-1010.88.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0026-CP627_997.575-1010.88.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8102710843086243</center></td>
  <td><center>0.6022943258285522</center></td>
</tr>
<tr>
  <td rowspan='3'>46</td>
  <td colspan='3'><b>Ivana, me diga uma coisa, você você está tendo o retorno do dos livros que você colocou aí na nas prateleiras, o Napoleão de Stendhal e o e o livro Mistério de Fazer Dinheiro, da da Nise Jinkings?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0062-CP716_579.784-592.628.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0062-CP716_579.784-592.628.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0062-CP716_579.784-592.628.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9587265253067017</center></td>
  <td><center>0.8845636248588562</center></td>
</tr>
<tr>
  <td rowspan='3'>47</td>
  <td colspan='3'><b>Mas isso, isso, digamos, que o Brasil passa hoje, que você teve referência, por exemplo, nesse seu estudo sobre o século dezessete, a elite, o poder no século dezessete, você acha que esse é o caminho, por exemplo, da história?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0127-CP572_1049.31-1061.16.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0127-CP572_1049.31-1061.16.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0127-CP572_1049.31-1061.16.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9493756294250488</center></td>
  <td><center>0.7579050660133362</center></td>
</tr>
<tr>
  <td rowspan='3'>48</td>
  <td colspan='3'><b>O público entra no estande, principalmente as crianças, eles estão... Você percebe alguma diferença no comportamento em relação à Bienal do Livro do Rio de Janeiro do ano passado, do ano retrasado para esta?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0021-CP558_405.056-416.718.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0021-CP558_405.056-416.718.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0021-CP558_405.056-416.718.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9567974805831909</center></td>
  <td><center>0.8313609957695007</center></td>
</tr>
<tr>
  <td rowspan='3'>49</td>
  <td colspan='3'><b>Eu gostaria de saber se se esses outros casos, se você acompanha isso, se, eh como é que você trataria disso se você fosse obrigado a colocar uma manchete oitenta por cento de inflação numa pesquisa em quatro supermercados?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0062-CP710_900.164-911.494.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0062-CP710_900.164-911.494.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0062-CP710_900.164-911.494.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9452207088470459</center></td>
  <td><center>0.8835744857788086</center></td>
</tr>
<tr>
  <td rowspan='3'>50</td>
  <td colspan='3'><b>e de um escritor alemão, quer dizer, você está batendo de frente com o gosto da literatura europeia e está conseguindo o seu espacinho lá, correto?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0028-CP671_459.64-470.809.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0028-CP671_459.64-470.809.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0028-CP671_459.64-470.809.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9493586421012878</center></td>
  <td><center>0.5857670307159424</center></td>
</tr>
<tr>
  <td rowspan='3'>51</td>
  <td colspan='3'><b>Tem coisa boa, quer dizer, o pai pode ficar, se se ele tiver interesse, ele pode entrar numa livraria, eh onde tiver livraria, pelo menos nas cidades do Brasil que tem livraria, né?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0067-CP698_963.154-973.92.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0067-CP698_963.154-973.92.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0067-CP698_963.154-973.92.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9084113836288452</center></td>
  <td><center>0.787875771522522</center></td>
</tr>
<tr>
  <td rowspan='3'>52</td>
  <td colspan='3'><b>Você acha que é importante para o estudo da literatura somente desse ponto de vista emocional, ou para o entendimento da própria literatura, por exemplo, da própria poesia do Manoel Bandeira, ou do Carlos Drummond de Andrade?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0060-CP520_998.982-1009.69.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0060-CP520_998.982-1009.69.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0060-CP520_998.982-1009.69.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9612194299697876</center></td>
  <td><center>0.8054676651954651</center></td>
</tr>
<tr>
  <td rowspan='3'>53</td>
  <td colspan='3'><b>Primeiro, eh quantas pessoas, no no no ápice da da da da comunidade, quantas pessoas moraram eh naquela região, em torno de Antônio Conselheiro?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0032-CP715_1164.78-1175.45.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0032-CP715_1164.78-1175.45.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0032-CP715_1164.78-1175.45.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9677669405937195</center></td>
  <td><center>0.7682552337646484</center></td>
</tr>
<tr>
  <td rowspan='3'>54</td>
  <td colspan='3'><b>Ô Jorge, é o seguinte, a gente esqueceu de avisar aí o pessoal que estava programado uma matéria a respeito de moral com Eva Blay, Irede Cardoso e Silva Pimentel, né?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0027-CP011_1250.69-1261.3.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0027-CP011_1250.69-1261.3.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0027-CP011_1250.69-1261.3.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9093436002731323</center></td>
  <td><center>0.7039867639541626</center></td>
</tr>
<tr>
  <td rowspan='3'>55</td>
  <td colspan='3'><b>que que acabam aparecendo num num num discurso, num num numa fase de pensamento, acabam passando para a sociedade, isso é como um pouquinho de jornalismo, um pouquinho infantilmente. ou ou ou</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0031-CP678_641.304-651.873.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0031-CP678_641.304-651.873.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0031-CP678_641.304-651.873.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.93729168176651</center></td>
  <td><center>0.8059520721435547</center></td>
</tr>
<tr>
  <td rowspan='3'>56</td>
  <td colspan='3'><b>Mas eu gostaria... Claudio, dá dá só uma uma uma aperfeiçoada na na sua colocação, de dessa geração que você colocou, de dessa da observação que você colocou.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0082-CP707_1508.09-1518.64.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0082-CP707_1508.09-1518.64.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0082-CP707_1508.09-1518.64.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9197467565536499</center></td>
  <td><center>0.7954109311103821</center></td>
</tr>
<tr>
  <td rowspan='3'>57</td>
  <td colspan='3'><b>Só só para encerrar a minha parte, é a pergunta do... A pergunta não, é uma uma indagação, até uma cobrança do ouvinte, o advogado João, aqui da da capital São Paulo.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0062-CP689_1588.32-1598.83.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0062-CP689_1588.32-1598.83.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0062-CP689_1588.32-1598.83.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9462858438491821</center></td>
  <td><center>0.8488016128540039</center></td>
</tr>
<tr>
  <td rowspan='3'>58</td>
  <td colspan='3'><b>Boa tarde Jorge Vasconcellos, boa tarde aos ouvintes da cê bê ene Brasil, mais uma edição do programa de livros e ideias, o Certas Palavras.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0005-CP711_37.016-47.463.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0005-CP711_37.016-47.463.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0005-CP711_37.016-47.463.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9461939334869385</center></td>
  <td><center>0.7777833938598633</center></td>
</tr>
<tr>
  <td rowspan='3'>59</td>
  <td colspan='3'><b>Eu te pergunto o seguinte, eh evidentemente, vamos assim, de contrário, qual era a visão do Fellini, isso é importante, é muito discutido, inclusive, dos meios de comunicação?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0014-CP524_647.095-657.541.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0014-CP524_647.095-657.541.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0014-CP524_647.095-657.541.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9406514167785645</center></td>
  <td><center>0.7378554344177246</center></td>
</tr>
<tr>
  <td rowspan='3'>60</td>
  <td colspan='3'><b>superadas, eu creio que já projetando para o próximo milênio, porque acho que até até noventa e nove vai ser impossível.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0075-CP719_1553.61-1563.93.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0075-CP719_1553.61-1563.93.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0075-CP719_1553.61-1563.93.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9039745330810547</center></td>
  <td><center>0.7340711355209351</center></td>
</tr>
<tr>
  <td rowspan='3'>61</td>
  <td colspan='3'><b>Até o próprio Ruy Castro, você pega uma uma reportagem feita com o Ruy Castro, de noventa e dois, acho que no Estadão, que ele diz, olha, quem tem menos de trinta anos no Brasil não sabe quem foi Leila Diniz, infelizmente.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0017-CP743_175.776-186.083.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0017-CP743_175.776-186.083.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0017-CP743_175.776-186.083.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9241275191307068</center></td>
  <td><center>0.7259863615036011</center></td>
</tr>
<tr>
  <td rowspan='3'>62</td>
  <td colspan='3'><b>Você deve ter esse tipo de experiência, eh mesmo porque, percorrendo o Brasil, você até contou, gostaria que até você contasse a história desse livro, que tem a ver com essa dificuldade de professora, né?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0013-CP665_98.747-109.014.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0013-CP665_98.747-109.014.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0013-CP665_98.747-109.014.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9674853086471558</center></td>
  <td><center>0.8752934336662292</center></td>
</tr>
<tr>
  <td rowspan='3'>63</td>
  <td colspan='3'><b>Um é da Nise, Nise? Nise Jenkins, que é O Mistério de Fazer Dinheiro, Automatização e Subjetividade no Trabalho Bancário.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0036-CP717_278.672-288.938.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0036-CP717_278.672-288.938.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0036-CP717_278.672-288.938.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9454936385154724</center></td>
  <td><center>0.9215831160545349</center></td>
</tr>
<tr>
  <td rowspan='3'>64</td>
  <td colspan='3'><b>Apesar de um pouco tardio, mas, eh tem seus motivos, você saberá porque, um balanço do que foi para o Brasil a Feira do Livro de Frankfurt de noventa e quatro.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0005-CP669_34.732-44.984.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0005-CP669_34.732-44.984.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0005-CP669_34.732-44.984.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9417672157287598</center></td>
  <td><center>0.8176150321960449</center></td>
</tr>
<tr>
  <td rowspan='3'>65</td>
  <td colspan='3'><b>Vamos, ehh digamos assim, aproximar para o momento agora, o digamos o, a pós-publicação e pós-premiação.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0066-CP707_1215.19-1225.44.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0066-CP707_1215.19-1225.44.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0066-CP707_1215.19-1225.44.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9480928182601929</center></td>
  <td><center>0.819366455078125</center></td>
</tr>
<tr>
  <td rowspan='3'>66</td>
  <td colspan='3'><b>Nós vamos conversar com o escritor e editor Paulo Condini, que é um um dos diretores da Cartago e Forte.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0008-CP676_31.909-42.157.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0008-CP676_31.909-42.157.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0008-CP676_31.909-42.157.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9055079817771912</center></td>
  <td><center>0.7885531187057495</center></td>
</tr>
<tr>
  <td rowspan='3'>67</td>
  <td colspan='3'><b>Eh, no no No Calabar, e que eu quer dizer eu lembro de alguma reportagem que tem falado da ajuda do seu pai ali na pesquisa do Calabar não sei se não não</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0020-CP009_533.245-543.487.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0020-CP009_533.245-543.487.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0020-CP009_533.245-543.487.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9077370762825012</center></td>
  <td><center>0.6759171485900879</center></td>
</tr>
<tr>
  <td rowspan='3'>68</td>
  <td colspan='3'><b>O caso de o do intelectual do dos países periféricos, digamos assim, ele como é que como é que ele se se situa idealmente, digamos?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0040-CP572_1488.78-1499.02.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0040-CP572_1488.78-1499.02.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0040-CP572_1488.78-1499.02.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9543161392211914</center></td>
  <td><center>0.7623214721679688</center></td>
</tr>
<tr>
  <td rowspan='3'>69</td>
  <td colspan='3'><b>do Vascaína Fi Firmo, o editor Firmo, mas que está lançando praticamente uma verdadeira coleção de livros sobre o Flamengo, textos de ficção e de história do Flamengo.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0081-CP697_1590.55-1600.77.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0081-CP697_1590.55-1600.77.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0081-CP697_1590.55-1600.77.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8978430032730103</center></td>
  <td><center>0.728082537651062</center></td>
</tr>
<tr>
  <td rowspan='3'>70</td>
  <td colspan='3'><b>Humberto, a primeira coisa que a gente gostaria de definir é o seguinte, o que é, para vocês, isso para o escritor, leitor, não ficar perdido, o que é um texto erótico?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0001-CP746_0.844-11.053.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0001-CP746_0.844-11.053.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0001-CP746_0.844-11.053.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.949688196182251</center></td>
  <td><center>0.6800419688224792</center></td>
</tr>
<tr>
  <td rowspan='3'>71</td>
  <td colspan='3'><b>Você diria que os militares, eh usando até um sp um termos de termo no no sentido hoje, atual, você diria que os militares do século passado eram mais progressistas, em certo sentido?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0027-CP651_636.957-647.141.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0027-CP651_636.957-647.141.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0027-CP651_636.957-647.141.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9481675624847412</center></td>
  <td><center>0.7965028285980225</center></td>
</tr>
<tr>
  <td rowspan='3'>72</td>
  <td colspan='3'><b>O Antônio Luiz, que é carioca, jornalista, advogado, administrador de empresas, professor e vice-presidente do conjunto universitário Cândido Mendes.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0013-CP646_825.087-835.232.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0013-CP646_825.087-835.232.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0013-CP646_825.087-835.232.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9314141869544983</center></td>
  <td><center>0.7081068158149719</center></td>
</tr>
<tr>
  <td rowspan='3'>73</td>
  <td colspan='3'><b>Você acha que se eh o Estado tivesse dado um pouco mais de livro para essas pessoas, um pouco menos de obrigações e mais livro, ah ahh a violência estaria amainada?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0067-CP746_1830.33-1840.44.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0067-CP746_1830.33-1840.44.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0067-CP746_1830.33-1840.44.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9398614168167114</center></td>
  <td><center>0.6706265211105347</center></td>
</tr>
<tr>
  <td rowspan='3'>74</td>
  <td colspan='3'><b>Marco Antônio, eh mas eh bom a figura central, digamos assim, seria inclusive o início do seu livro, parte da figura central, de Antônio Conselheiro, perfeito é.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0011-CP715_150.883-160.971.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0011-CP715_150.883-160.971.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0011-CP715_150.883-160.971.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9660453796386719</center></td>
  <td><center>0.7466484904289246</center></td>
</tr>
<tr>
  <td rowspan='3'>75</td>
  <td colspan='3'><b>Ricardo Viveiros, poeta jornalista, como já lembramos no decorrer de todo esse programa, autor do do reeditado, agora reeditado, em quarta edição,</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0080-CP551_1318.68-1328.75.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0080-CP551_1318.68-1328.75.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0080-CP551_1318.68-1328.75.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9333884716033936</center></td>
  <td><center>0.7574089169502258</center></td>
</tr>
<tr>
  <td rowspan='3'>76</td>
  <td colspan='3'><b>Hoje, dia quatorze de março, um sábado com muita preguiça, Certas Palavras voltas volta para falar de livros.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0002-CP002_62.998-73.023.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0002-CP002_62.998-73.023.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0002-CP002_62.998-73.023.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.7598262429237366</center></td>
  <td><center>0.6696453094482422</center></td>
</tr>
<tr>
  <td rowspan='3'>77</td>
  <td colspan='3'><b>escritora, roteirista de tê vê, roteirista de audiovisuais, que pela editora Companhia das Letras lançou recentemente aqui em São Paulo o livro Acqua-toffana.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0004-CP649_48.78-58.457.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0004-CP649_48.78-58.457.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0004-CP649_48.78-58.457.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8881415128707886</center></td>
  <td><center>0.6325013637542725</center></td>
</tr>
<tr>
  <td rowspan='3'>78</td>
  <td colspan='3'><b>Quando trata-se aqui do livro Reformas Econômicas e Novas Democracias, acredito que seja exatamente o Brasil, Portugal, Grécia, Espanha, principalmente esses quatro países. Eh</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0041-CP678_884.368-894.038.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0041-CP678_884.368-894.038.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0041-CP678_884.368-894.038.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9412482380867004</center></td>
  <td><center>0.7728475332260132</center></td>
</tr>
<tr>
  <td rowspan='3'>79</td>
  <td colspan='3'><b>A apresentação do Juva, com o seu verso da língua, é do Veríssimo e o do do do Rodrigo Lacerda, do João Baldo Ribeiro.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0011-CP697_144.759-154.402.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0011-CP697_144.759-154.402.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0011-CP697_144.759-154.402.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9580930471420288</center></td>
  <td><center>0.7849447727203369</center></td>
</tr>
<tr>
  <td rowspan='3'>80</td>
  <td colspan='3'><b>E ontem nós prometemos um programa histórico, dois programas históricos, certas palavras, para lá da Colônia, né, para lá do Brasil Colônia. Ontem nós</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0004-CP549_33.149-42.733.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0004-CP549_33.149-42.733.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0004-CP549_33.149-42.733.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9383188486099243</center></td>
  <td><center>0.771982729434967</center></td>
</tr>
<tr>
  <td rowspan='3'>81</td>
  <td colspan='3'><b>Mas o seu pai, de alguma forma, no em algum trabalho seu, do teatro, alguma pesquisa sua, contribuiu em alguma em alguma eh alguma algum trabalho ai alguma peça, alguma coisa?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0022-CP009_546.348-555.93.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0022-CP009_546.348-555.93.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0022-CP009_546.348-555.93.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.867875337600708</center></td>
  <td><center>0.6576130390167236</center></td>
</tr>
<tr>
  <td rowspan='3'>82</td>
  <td colspan='3'><b>Quer dizer, saber que você vai escrever, vai ter um monte de lauda na sua frente, vai ter que entregar para um editor, vai ter todo um processo, vai ter todo uma briga, pesa para você isso?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0018-CP575_323.46-333.031.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0018-CP575_323.46-333.031.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0018-CP575_323.46-333.031.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9054410457611084</center></td>
  <td><center>0.6994327902793884</center></td>
</tr>
<tr>
  <td rowspan='3'>83</td>
  <td colspan='3'><b>A Ilda Rios, de uma vez, disse, num certas palavras, que o livro ele servia para ela, um um uma das funções principais do livro, como um escudo contra a violência.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0065-CP746_1818.31-1827.88.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0065-CP746_1818.31-1827.88.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0065-CP746_1818.31-1827.88.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9353285431861877</center></td>
  <td><center>0.7185570001602173</center></td>
</tr>
<tr>
  <td rowspan='3'>84</td>
  <td colspan='3'><b>entre a gente e a editora, e que nós estaremos, eh, telefonando para essas pessoas durante essa semana e elas receberão os seus livros em casa, está certo?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0119-CP572_895.156-904.004.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0119-CP572_895.156-904.004.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0119-CP572_895.156-904.004.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9373169541358948</center></td>
  <td><center>0.7712700366973877</center></td>
</tr>
<tr>
  <td rowspan='3'>85</td>
  <td colspan='3'><b>Então, do ponto de vista histórico e literário, eh, de onde vem o gosto do mineiro pela escrita, principalmente pelo conto, pelo caso?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0075-CP575_837.663-846.505.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0075-CP575_837.663-846.505.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0075-CP575_837.663-846.505.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9266843199729919</center></td>
  <td><center>0.7385190725326538</center></td>
</tr>
<tr>
  <td rowspan='3'>86</td>
  <td colspan='3'><b>Eu gostaria que o senhor falasse um pouco disso, do jeito do livro, eu tenho como é que se que se montou, né?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0063-CP745_1244.26-1253.1.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0063-CP745_1244.26-1253.1.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0063-CP745_1244.26-1253.1.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8737387657165527</center></td>
  <td><center>0.7999476194381714</center></td>
</tr>
<tr>
  <td rowspan='3'>87</td>
  <td colspan='3'><b>Acho que quanto mais você o o o computador avança, mais você fica você fica maravilhado com a facilidade de manipulação do livro.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0079-CP703_1363.48-1372.31.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0079-CP703_1363.48-1372.31.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0079-CP703_1363.48-1372.31.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9671940803527832</center></td>
  <td><center>0.8530583381652832</center></td>
</tr>
<tr>
  <td rowspan='3'>88</td>
  <td colspan='3'><b>A poesia de Safo, a poesia grega em geral, é uma poesia na qual o a a palavra é uma, de uma certa maneira, a manifestação do Deus.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0071-CP623_806.81-815.597.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0071-CP623_806.81-815.597.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0071-CP623_806.81-815.597.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9348686933517456</center></td>
  <td><center>0.7009700536727905</center></td>
</tr>
<tr>
  <td rowspan='3'>89</td>
  <td colspan='3'><b>A escravidão acabou, a vida cotidiana dos escravos, negritude e sexualidade. O Certas Palavras vai para o intervalo, mas volta já já</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0012-CP663_497.779-506.47.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0012-CP663_497.779-506.47.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0012-CP663_497.779-506.47.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8951704502105713</center></td>
  <td><center>0.7430290579795837</center></td>
</tr>
<tr>
  <td rowspan='3'>90</td>
  <td colspan='3'><b>Não, dá um trabalho de recorte ali, de usar material que foi, que eu lembro de ter lido na página dele, nessa página que falamos, o Diário da Corte,</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0029-CP524_1623.56-1632.19.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0029-CP524_1623.56-1632.19.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0029-CP524_1623.56-1632.19.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8521625995635986</center></td>
  <td><center>0.6488885879516602</center></td>
</tr>
<tr>
  <td rowspan='3'>91</td>
  <td colspan='3'><b>inclusive de alguns éh que estiveram em campos de concentração, mas que fazem parte realmente da sua família, quer dizer, isso é isso é um dado biográfico concreto.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0014-CP547_119.472-127.723.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0014-CP547_119.472-127.723.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0014-CP547_119.472-127.723.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9415075182914734</center></td>
  <td><center>0.7940635681152344</center></td>
</tr>
<tr>
  <td rowspan='3'>92</td>
  <td colspan='3'><b>eh, Depois que conseguiram a a igualdade nas escolas, no ônibus, esse tipo de coisa, que teve aquela quebradeira, tudo estava sem rumo, quer dizer, não sabia o que fazer.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0050-CP637_1070.41-1078.63.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0050-CP637_1070.41-1078.63.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0050-CP637_1070.41-1078.63.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9334032535552979</center></td>
  <td><center>0.8874996900558472</center></td>
</tr>
<tr>
  <td rowspan='3'>93</td>
  <td colspan='3'><b>Por exemplo, esteve aqui a ah Ana Maria Machado, voltando de uma viagem, exatamente, que ela fez, acho que com vinte escritores, é isso?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0061-CP679_881.33-889.512.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0061-CP679_881.33-889.512.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0061-CP679_881.33-889.512.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9253876209259033</center></td>
  <td><center>0.6849582195281982</center></td>
</tr>
<tr>
  <td rowspan='3'>94</td>
  <td colspan='3'><b>Exatamente, olha eh um... Preocupado até com o público... Ah, não vou explicar melhor isso... não ou não?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0048-CP551_690.459-698.622.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0048-CP551_690.459-698.622.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0048-CP551_690.459-698.622.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8942857980728149</center></td>
  <td><center>0.7813974618911743</center></td>
</tr>
<tr>
  <td rowspan='3'>95</td>
  <td colspan='3'><b>Foi nesse contraponto que eu tentei compreender a modernidade eh ligada a ao mundo arcaico de Safo de Lesbos.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0079-CP623_853.479-861.621.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0079-CP623_853.479-861.621.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0079-CP623_853.479-861.621.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.8960597515106201</center></td>
  <td><center>0.6733695268630981</center></td>
</tr>
<tr>
  <td rowspan='3'>96</td>
  <td colspan='3'><b>Sidney, mais um minutinho, porque nós vamos fazer novamente o nosso Jornalismo Eletrônico ao Vivo, agora direto do Canadá, com Oscar Ulisses.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0015-CP648_689.891-698.017.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0015-CP648_689.891-698.017.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0015-CP648_689.891-698.017.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9045847654342651</center></td>
  <td><center>0.7357562780380249</center></td>
</tr>
<tr>
  <td rowspan='3'>97</td>
  <td colspan='3'><b>Nelly, vamos dar uma ideia do livro, inclusive professores, educadores do Brasil inteiro, eh, bibliotecários, têm que ter esse livro à mão, né?</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0034-CP725_600.568-608.671.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0034-CP725_600.568-608.671.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0034-CP725_600.568-608.671.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9423266649246216</center></td>
  <td><center>0.8577660918235779</center></td>
</tr>
<tr>
  <td rowspan='3'>98</td>
  <td colspan='3'><b>que é o fato de que, ainda bem que você fez tudo nesse livro do jeito que você fez eh.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0015-CP720_1248.02-1256.1.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0015-CP720_1248.02-1256.1.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0015-CP720_1248.02-1256.1.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9447859525680542</center></td>
  <td><center>0.8874790668487549</center></td>
</tr>
<tr>
  <td rowspan='3'>99</td>
  <td colspan='3'><b>Talvez hoje não houvesse con eh con condição propícia para uma Leila Diniz, mesmo no Rio de Janeiro.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0038-CP743_470.678-478.742.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0038-CP743_470.678-478.742.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0038-CP743_470.678-478.742.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9058036208152771</center></td>
  <td><center>0.6489541530609131</center></td>
</tr>
<tr>
  <td rowspan='3'>100</td>
  <td colspan='3'><b>Cerca aí de sete minutos, nós ainda estamos na pergunta do ouvinte Carlos Alberto Barbosa, estudante lá de Guaianases, de Guarulhos.</b></td>
</tr>
<tr>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='ground_truth/0054-CP572_1823.22-1831.28.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='yt-fn-cml/sr16k_mono_0054-CP572_1823.22-1831.28.wav_synthesized.wav' type='audio/mpeg'></audio></td>
  <td><audio controls preload style='width: 150px; height:40px;'><source src='f5-fn-cv/cv-fn_0054-CP572_1823.22-1831.28.wav' type='audio/mpeg'></audio></td>
</tr>
<tr>
  <td><center><b>Similaridade:</b></center></td>
  <td><center>0.9359356164932251</center></td>
  <td><center>0.7770459651947021</center></td>
</tr>
</tbody>
</table>