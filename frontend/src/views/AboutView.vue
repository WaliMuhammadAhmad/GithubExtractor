<script setup lang="ts">
import Footer from '@/components/Footer.vue'
</script>

<template>
  <div class="container">
    <section class="aboutSection">
      <div>
        <h1 class="heading">Overview</h1>
        <p>
          This project is designed to help developers extract JUnit test cases from their codebase
          efficiently. It leverages GitHub's features to streamline the process and ensure that your
          tests are always up-to-date with the latest changes in your repository.
        </p>
      </div>
      <img src="/images/github-apple.png" alt="" />
    </section>
    <section class="diffSection">
      <h1 class="heading">Github Repositories Details Extractor</h1>
      <p>
        This tool allows you to search for public repositories on GitHub and extract details such as
        the number of stars, forks, issues, and pull requests. It also provides a list of
        contributors and the latest commits to the repository. This tool is designed to make it
        easier for you to get the information you need from GitHub repositories.
      </p>
      <p>
        The tool works by taking user requirements or queries and sending them to the GitHub API,
        which fetches the repository details. The number of repositories fetched is fixed at a
        maximum of 1000, but the minimum can be any number. Users can get personalized information
        such as star count, fork count, and other redundant information that may be useful depending
        on the use case. Additionally, users can download the results as a CSV file to their local
        system.
      </p>
    </section>
    <section class="restSection">
      <h1 class="heading">Java Focal Methods Extractor</h1>
      <p>
        This tool allows you to extract focal methods and their corresponding JUnit test cases from
        Java repositories on GitHub. It is designed to help you identify the most important methods
        in your codebase and ensure that they are properly tested. The tool works by analyzing the
        code in the repository and identifying methods that are likely to be focal methods. It then
        extracts these methods and their corresponding test cases, allowing you to review them and
        make any necessary changes.
      </p>
      <p>
        The tool uses a combination of static analysis and machine learning techniques to identify
        focal methods and their corresponding test cases. It analyzes the code in the repository to
        identify methods that are likely to be focal methods based on factors such as complexity,
        frequency of use, and importance to the overall functionality of the code. It then extracts
        these methods and their corresponding test cases, allowing you to review them and make any
        necessary changes.
      </p>
    </section>
    <section class="diffSection">
      <h1 class="heading">About the Developer</h1>
      <p>
        This project is developed with dedication and effort to make the life of developers easier.
        Follow the developer on social media to stay updated with the latest features and
        improvements.
      </p>
      <div class="developerInfo">
        <a href="https://gravatar.com/walimuhammadahmad">
          <img
            class="profile"
            src="https://1.gravatar.com/avatar/40fc6c82e8df213fcf8a4943d580fe9dc3fe2d991dcb9fd66a3a23055901e7f6?size=512"
            alt="Developer Gravatar"
          />
        </a>
        <q class="developerBio">
          I'm a student studying software engineering, and I really love doing research and creating
          new things. It's like my favorite game, exploring and making stuff in the world of
          computers!
        </q>
      </div>
    </section>
  </div>
  <section>
    <Footer />
  </section>
</template>

<style scoped>
.aboutSection {
  min-height: 100vh;
  display: flex;
  align-items: center;
}
img {
  width: 40dvw;
}
.heading {
  font-size: 4rem;
  letter-spacing: -4px;
  line-height: 1;
  font-weight: bold;
  margin-bottom: 1rem;
}
.restSection {
  min-height: 100vh;
  height: fit-content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  font-size: 1.5rem;
}
.diffSection {
  min-height: 100dvh;
  height: fit-content;
  background-color: hsla(160, 100%, 37%, 0.2);
  border: 2px solid hsla(160, 100%, 37%, 0.2);
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 2rem;
  gap: 2rem;
  font-size: 1.5rem;
}
.developerInfo {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  gap: 2rem;
  width: 70%;
}
.profile {
  border-radius: 50%;
  width: 15rem;
  height: 15rem;
}
.developerBio {
  font-size: 1.2rem;
  display: flex;
  flex-direction: column;
}

@media (max-width: 768px) {
  .diffSection {
    padding: 2rem;
    font-size: 1.2rem;
  }
  .restSection {
    padding: 2rem 0;
    font-size: 1.2rem;
  }
  .developerInfo {
    width: 100%;
    gap: 1rem;
  }
}

@media (max-width: 525px) {
  .heading {
    font-size: 3rem;
    letter-spacing: -3px;
  }
  .aboutSection {
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
  }
  .developerInfo {
    flex-direction: column;
  }
  img {
    width: 70dvw;
  }
}

@media (max-width: 425px) {
  .heading {
    font-size: 2rem;
    letter-spacing: -2px;
  }
  .aboutSection {
    gap: 1rem;
  }
  .restSection {
    min-height: fit-content;
    padding: 1rem;
    gap: 1rem;
    font-size: 1rem;
  }
  .diffSection {
    min-height: fit-content;
    padding: 1rem;
    gap: 1rem;
    font-size: 1rem;
  }
  .developerBio {
    font-size: 1rem;
  }
}
</style>
