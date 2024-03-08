# Microchallenge 2 - Crystal Ball 
## Experiencing Sustainable Futures through AI-Powered Visualization
Jorge, Sophie and Dhrishya

## Ideation

### Initial Interests

![Screenshot 2024-03-08 141203](https://github.com/sophma/microchallenge2/assets/147055292/01246612-d7fb-4fd8-8c1f-30c69fea2830)

We formed our group based on our common interests of speculative future visualisation, better policymaking and civic engagement and the potential of emerging generative AI technilogies.

### Concept

We want to introduce innovation into the sector of policymaking and civic engagement by creating a technology that would enable users to visualise and experience the future impact of policy interventions, creating avenues for innovative civic feedback mechanisms for better policymaking. The technology would be supported by AI, and would use a specific foresight methodology to envision possible future scenarios for a given picture, based on planned policy interventions. For the purpose of this microchallenge, we chose EU policy roadmaps for building renovation, smart and sustainable mobility, more inclusive and sustainable living spaces, and the circular economy.

![Screenshot 2024-03-08 151854](https://github.com/sophma/microchallenge2/assets/147055292/b074c391-496f-4988-86a2-140ba930b337)


### References

https://environment.ec.europa.eu/strategy/circular-economy-action-plan_en
https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficient-buildings/renovation-wave_en
https://new-european-bauhaus.europa.eu/index_en
https://transport.ec.europa.eu/transport-themes/mobility-strategy_en
https://www.ifforesight.com/whatis-orion
https://furnitures.dottod.net/
https://bjoernkarmann.dk/project/paragraphica
https://foresightguide.com/dator-four-futures/
https://www.researchgate.net/publication/228380947_Alternative_futures_at_the_Manoa_School

### Planning

### Integrated Design

## Process

### Iteration 1 - Cystal Ball Custom GPT

![Screenshot 2024-03-08 151854](https://github.com/sophma/microchallenge2/assets/147055292/19d0e685-47e0-415a-8861-23d3c57bb8bd)

We first wanted to go through the entire process with a custom bot built on ChatGPT 4 to test the workflow and see if we could get to a final output. We trained a custom bot with Dator and Smart's future archetypes foresight methodology and gave the EU policy documents as input (Renovation Wave, EU Circular Economy Plan, Smart and Sustainable Mobility Strategy, New EU Bauhaus). The bot was trained to perform a foresight analysis based on the EU policy documents  We had to reconfigure the bot several times to get to the optimal output. As we weren't satisfied with OpenAI's future image output, we decided to use another [AI model]([url](https://huggingface.co/spaces/tonyassi/image-to-image-SDXL)) using stable diffusion, which was better at doing image to image outputs. 

![WhatsApp Image 2024-03-06 at 10 34 53 (1)](https://github.com/sophma/microchallenge2/assets/147055292/66ff4323-3204-46ef-bd4a-18499b49d33d)
![32185232-aa1b-4440-8454-bee88d2ce343](https://github.com/sophma/microchallenge2/assets/147055292/66f9cb23-26c6-4f5e-a7a6-9a2ebad75fc9)
![df62b106-d833-40d5-b03a-6e748293070b](https://github.com/sophma/microchallenge2/assets/147055292/5a1e4548-3c8e-442f-a895-bc93c7c4365f)


### Iteration 2 -  Modmatrix to Crystal Ball interface

![Screenshot 2024-03-08 154729](https://github.com/sophma/microchallenge2/assets/147055292/98753a1c-0ae6-4d5f-8802-96920c7a81c5)

We wanted to make the entire experience automatic for users who do not have ChatGPT 4 so we decided to created an interface that would integrate the entire process. We used Modmatrix's source code and adapted it to create our own Crystal Ball interface on Replit. We used OpenAI's API to describe the input image and undertake the foresight analysis based on the EU policy documents but we couldn't use the stable diffusion model to create the future image as it wasn't open source. So we found another image to image model on [replicate]([url](https://replicate.com/stability-ai/sdxl)https://replicate.com/stability-ai/sdxl) that could be integrated in the interface with an API. As the ultimate aim was to showcase this future scenario through an immersive experience, we worked with 360-like images.

![0c55eebb-c70d-4e89-a99b-b0c3e6b2303e (1)](https://github.com/sophma/microchallenge2/assets/147055292/379c62fb-dac2-4584-9bda-e5882aaab01a)
![6d39fb57-a442-48f2-976c-62e3c838df3f (1)](https://github.com/sophma/microchallenge2/assets/147055292/480ff7f4-fbbe-42cd-8a88-4ab688409c2f)

Original image: 
![b4f72323-4729-487a-90cf-ca627cffdb7d](https://github.com/sophma/microchallenge2/assets/147055292/88215f05-5575-429d-84d2-cf7d916f7dbb)


Original image + video: 
![b4f72323-4729-487a-90cf-ca627cffdb7d](https://github.com/sophma/microchallenge2/assets/147055292/4efafeb9-fa63-4bc5-a87e-a867433cdac4)


Transformed image: 
![2831beaa-f6d7-4169-a036-5a651f2367a0](https://github.com/sophma/microchallenge2/assets/147055292/72cb11c0-0924-479e-8577-5c57a713adf4)


### Code

### Final Conclusions
The technology needs to be more mature for the experience to become optimal. The product will evolve as the AI models used evolve.
We think there is a lot of potential for this project as this can bring in more experimental approaches to policymaking and decisionmaking overall, as this could also be used in other environments. By making the feedback mechanism more immersive, this tool can also help citizens be more aware and involved in policy as it makes policy jargon more accessible.

### Opportunities for Future Development
As the state-of-the-art technology evolves, we want to create different ways to showcase this future scenario to enable different feedback processes: through virtual reality, through video, through image portals in the city, through physical objects present in the virtual scenarios etc.
We also want to create experiences where different types of stakeholders could provide feedback, and automatize the feedback collection.
We want to reach out to stakeholders of relevance in the policy sector and in the civic community to test our product.
 
