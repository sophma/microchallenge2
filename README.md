# Microchallenge 2 - Crystal Ball 
## Experiencing Sustainable Futures through AI-Powered Visualization
Jorge, Sophie and Dhrishya

## Ideation

### Initial Interests

![Screenshot 2024-03-08 162049](https://github.com/sophma/microchallenge2/assets/147055292/654bfc1e-1ea7-4007-b145-c38483291759)

We formed our group based on our common interests of speculative future visualisation, better policymaking and civic engagement and the potential of emerging generative AI technologies.

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
![Screenshot 2024-04-01 222540](https://github.com/sophma/microchallenge2/assets/147055292/66d38ae1-2bd3-4c6e-bdc2-1d4e36e64801)

### Integrated Design
As we wanted to make the tool accessible to a maximum number of people, we decided to opt for an immersive experience that could be accessed through the phone instead of VR glasses. The images of future scenarios were obtained thanks to generative AI, but then we used the website [glitch]([url](https://glitch.com/)) to create virtual environments that can be accessed through a link. We also built an automated and integrated version of the entire process with Modmatrix, so that anyone could generate future scenarios on their own.

## Process

### Iteration 1 - Cystal Ball Custom GPT

![Screenshot 2024-03-08 163057](https://github.com/sophma/microchallenge2/assets/147055292/d1a51b89-a30b-42a7-891f-04270a121017)


We first wanted to go through the entire process with a custom bot built on ChatGPT 4 to test the workflow and see if we could get to a final output. We trained a custom bot with Dator and Smart's future archetypes foresight methodology and gave the EU policy documents as input (Renovation Wave, EU Circular Economy Plan, Smart and Sustainable Mobility Strategy, New EU Bauhaus). The bot was trained to perform a foresight analysis based on the EU policy documents  We had to reconfigure the bot several times to get to the optimal output. As we weren't satisfied with OpenAI's future image output, we decided to use another [AI model]([url](https://huggingface.co/spaces/tonyassi/image-to-image-SDXL)) using stable diffusion, which was better at doing image to image outputs. 

#### Custom GPT output:

**Image Input:**
![WhatsApp Image 2024-03-06 at 10 34 53 (1)](https://github.com/sophma/microchallenge2/assets/147055292/66ff4323-3204-46ef-bd4a-18499b49d33d)

**Image Description:**

The image depicts an urban street scene on what appears to be a sunny day with a mix of clouds. On the left side of the street, there are leafless trees, indicating either winter or early spring before the foliage has returned. There is a street lamp and a small red building with large glass windows, resembling a shop or small commercial building. On the right side, there are taller buildings, seemingly residential or commercial, with a mixture of architectural styles and states of maintenance. One of the buildings is undergoing construction or renovation, as indicated by the scaffolding on its facade. The street itself is quite busy with a row of parked motorcycles at the forefront, a taxi, and other vehicles further down the road. There is a clear pedestrian crossing leading towards the buildings. The image gives an impression of a bustling urban area during a non-peak time of the day.

**Foresight analysis:**

STEEPV Analysis:

Social: The area appears to be a mixed-use neighborhood with both commercial and residential spaces. The density of motorcycles suggests a reliance on motorized individual transport, possibly indicative of social behaviors and the demands of city life.
Technological: Visible street lamps could be replaced with more energy-efficient lighting. The construction scaffolding indicates ongoing development, possibly for renovation or modernization.
Economic: The presence of commercial activity, as indicated by the storefronts, suggests economic vitality. Renovation efforts could imply investment into the area, signaling economic growth or regeneration.
Environmental: Leafless trees may suggest an opportunity for increased greenery to combat urban heat islands. The use of construction materials in the renovation could be assessed for environmental impact.
Political: Policy decisions may influence the kind of renovation taking place, as well as transportation management in the city, particularly the prevalence of motorcycles and a taxi, which may be subject to urban transport regulations.
Values: The area reflects practical urban design, but it may benefit from aesthetic and community-driven improvements that align with the values of sustainability and social inclusion.
Signals:
Strong Signals: Renovation efforts, heavy reliance on personal motorized vehicles.
Weak Signals: Possible need for more inclusive urban spaces, potential shift towards more sustainable transport solutions.
Critical Uncertainties:

Will the renovations lead to more sustainable and energy-efficient buildings?
Is there a trend towards improving urban green spaces in this area?
How might policies evolve to address the evident transportation modes and needs?
Next, I will describe detailed future scenarios based on the archetypes of continued growth, collapse, disciplined society, and transformation. Following that, you may choose a preferred scenario, and I will modify the initial description of the picture to reflect that scenario.

**Future Scenarios:**

1. Continued Growth:
The bustling urban street becomes the epitome of eco-modernist vision. By 2050, this street, once dominated by combustion-engine motorcycles, now thrives with electric bikes and scooters, all neatly docked at solar-powered charging stations. The red building, a former shop, is now a community hub for the exchange of goods and services, operating on a circular economy model. The upper floors are retrofitted with green walls, contributing to air purification and biodiversity. The construction scaffolding is part of a larger initiative to integrate energy-efficient solutions into existing structures, symbolizing the city's commitment to merging historical aesthetic with sustainable innovation. The urban forestry initiative has ensured that trees are now lush, providing shade and reducing the urban heat island effect. Public spaces are reimagined as green corridors, encouraging walking and cycling, and the cityscape is punctuated by pocket parks and urban farms.

2. Collapse:
In this scenario, the street reflects the failure to address climate change adequately. The small red building has been abandoned, the glass dulled and cracked. The motorcycles, relics of a past era, are rusting, with the city's population unable to sustain their maintenance due to economic collapse. The taller buildings are in disrepair, their facades crumbling, scaffolding left as skeletal reminders of halted progress. The streets are empty, the infrastructure is failing, and the urban trees are dead, victims of extreme weather conditions and neglect. This future serves as a stark warning of what could happen if sustainable initiatives like the New European Bauhaus are not embraced and acted upon urgently.

3. Disciplined Society:
By 2050, discipline defines the urban environment. The street has been transformed into a model of efficiency and sustainability. The red building is now an energy-positive facility, its roof lined with solar panels. Strict regulations limit the use of personal vehicles, evident in the absence of motorcycles; instead, residents rely on a highly efficient and clean public transit system, visible from the electric buses gliding silently by. Buildings are renovated to meet exacting energy standards, with the construction site showcasing the latest in low-carbon materials and technology. Trees are pruned and managed meticulously to optimize their environmental contributions, and pedestrian zones dominate the landscape, minimizing the need for mechanized transport.

4. Transformation:
A radical transformation of urban living by 2050 paints a new picture. Technological advancements have revolutionized transport, with autonomous vehicles and drones, which cannot be seen in the image but are implied, ensuring efficient and clean movement of people and goods. The red building is now a community tech center, where residents share knowledge and skills for a resilient future. The building under renovation is being transformed into a mixed-use space with communal living areas, workshops, and vertical farms, all powered by renewable energy. Infrastructure is designed to be multi-functional, with roads doubling as water capture and filtration systems. The leafless trees have been replaced by genetically modified varieties that thrive in urban conditions and provide more greenery.

**Future Image Description:**

In the disciplined society scenario by 2050, the urban street scene has undergone a transformation emphasizing efficiency, sustainability, and regulatory compliance, while upholding a high standard of urban living. The once-commercial red building has been repurposed into an energy-positive facility, its roof equipped with an array of solar panels feeding clean energy back into the grid. Where motorcycles once lined the curb, there are now designated spaces for shared electric vehicles, including bikes and scooters, encouraging residents to engage with the city's comprehensive and clean public transportation system.

The buildings flanking the streets display facades retrofitted with advanced insulation materials and self-cleaning air-purifying surfaces, reducing the urban heat island effect and cutting down energy consumption. Windows that automatically adjust their tint based on the sunlight's intensity are now standard, maximizing natural light while minimizing heat gain. The ongoing construction is part of a city-wide initiative to update all buildings with such smart materials, as well as to integrate green infrastructure and technology into the existing urban fabric.

Mature trees have been strategically planted to optimize air quality and provide shaded walkways, promoting pedestrian traffic. Communal gardens and vertical farming units are interspersed throughout the neighborhood, enhancing both the aesthetics and the local food production, thus reducing food miles.

Transportation has been revolutionized, with the taxi and personal vehicles replaced by autonomous electric shuttles, which glide silently along the priority lanes reserved for clean transportation. All road surfaces are now constructed with photocatalytic concrete that helps to clean the air and break down pollutants. Digital displays embedded in sidewalks provide residents with real-time information on public transportation schedules, community news, and environmental quality indicators.

Under the disciplined society scenario, the urban environment becomes a testament to the possibilities of stringent planning, technological integration, and communal effort towards achieving a sustainable and orderly future. This scenario underscores the role of effective governance and the collective adoption of sustainable practices in shaping urban areas to be resilient and in harmony with broader environmental goals.

**OpenAI Future Image Output:**
![32185232-aa1b-4440-8454-bee88d2ce343](https://github.com/sophma/microchallenge2/assets/147055292/66f9cb23-26c6-4f5e-a7a6-9a2ebad75fc9)

**Stable Diffusion Image Output:**
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


### Final Conclusions
The technology needs to be more mature for the experience to become optimal. The product will evolve as the AI models used evolve.
We think there is a lot of potential for this project as this can bring in more experimental approaches to policymaking and decisionmaking overall, as this could also be used in other environments. By making the feedback mechanism more immersive, this tool can also help citizens be more aware and involved in policy as it makes policy jargon more accessible.

### Opportunities for Future Development
As the state-of-the-art technology evolves, we want to create different ways to showcase this future scenario to enable different feedback processes: through virtual reality, through video, through image portals in the city, through physical objects present in the virtual scenarios etc.
We also want to create experiences where different types of stakeholders could provide feedback, and automatize the feedback collection.
We want to reach out to stakeholders of relevance in the policy sector and in the civic community to test our product.

### Summary of Problems Encountered
- OpenAI did not produce the expected visualisations of future scenarios. All images rendered by the custom bot were similar as the bot could not understand that modifications should be done to the original picture. To overcome this challenge, we used a stable diffusion AI model which gave much better images.
- Coding the Crystal Ball Modmatrix was more challenging than expected. We ran into the problem of having too many tokens requested for the type of API we had, so the future scenarios could not be generated. To be able to finalise the tool, we had to pay to upgrade our API access, which we decided not to do.

### Design boundaries and personal contributions
This project is a reflection of the complementarity of each member of our team: coming from a policy background, I contributed to the policy angle of the project and the different policy programmes that needed to be fed to the AI. Having a bit of experience with coding, I also contributed to the design of the Crystal Ball tool. Jorge has significant experience in foresight studies and emerging technologies and contributed significantly to the technical and methodological aspects of the project, including coding the Crystal Ball tool. Having more experience with computational modeling, Dhrishya contributed to the visualisation of images as well as research.



 
