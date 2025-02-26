<script setup lang="ts">
import Footer from '@/components/Footer.vue'
import languages from '@/data/languages'
import licenses from '@/data/license'
import { useReposForm } from '@/api/reposForm'

const { reposForm, reqRepos } = useReposForm()
</script>

<template>
  <div class="container">
    <section>
      <div class="section">
        <h1 class="heading">Get the list of public repositories from Github</h1>
        <div class="diffSection">
          <form @submit.prevent="reqRepos" method="post">
            <!-- Starter -->
            <fieldset>
              <legend>Starter</legend>
              <div class="grid">
                <!-- Language -->
                <div class="col">
                  <label for="language">Language</label>
                  <select
                    style="text-transform: capitalize"
                    name="language"
                    id="language"
                    v-model="reposForm.language"
                    required
                  >
                    <option v-for="language in languages" :key="language" :value="language">
                      {{ language }}
                    </option>
                  </select>
                </div>

                <!-- Created Date -->
                <div class="col">
                  <label for="created-date">Created Date</label>
                  <input
                    type="date"
                    name="created"
                    id="created-date"
                    v-model="reposForm.created"
                    aria-label="Select repository creation date"
                  />
                </div>

                <!-- Pushed Date -->
                <div class="col">
                  <label for="pushed-date">Pushed Date</label>
                  <input
                    type="date"
                    name="pushed"
                    id="pushed-date"
                    v-model="reposForm.pushed"
                    aria-label="Select repository last pushed date"
                  />
                </div>
              </div>
            </fieldset>

            <!-- Keywords -->
            <fieldset>
              <legend>Keywords</legend>
              <div class="grid">
                <div class="col">
                  <label for="repo-name">Name</label>
                  <input
                    type="text"
                    name="name"
                    id="repo-name"
                    v-model="reposForm.name"
                    placeholder="e.g., flask"
                    maxlength="15"
                    aria-label="Enter repository name"
                  />
                </div>
                <div class="col">
                  <label for="repo-description">Description</label>
                  <input
                    type="text"
                    name="description"
                    id="repo-description"
                    v-model="reposForm.description"
                    placeholder="e.g., web framework"
                    maxlength="56"
                    aria-label="Enter repository description"
                  />
                </div>
                <div class="col">
                  <label for="repo-readme">Readme</label>
                  <input
                    type="text"
                    name="readme"
                    id="repo-readme"
                    v-model="reposForm.readme"
                    placeholder="e.g., installation"
                    maxlength="32"
                    aria-label="Enter text from README"
                  />
                </div>
                <div class="col">
                  <label for="repo-owner">Owner</label>
                  <input
                    type="text"
                    name="owner"
                    id="repo-owner"
                    v-model="reposForm.owner"
                    placeholder="e.g., pallets"
                    maxlength="15"
                    aria-label="Enter repository owner"
                  />
                </div>
                <div class="col">
                  <label for="repo-user">User</label>
                  <input
                    type="text"
                    name="user"
                    id="repo-user"
                    v-model="reposForm.user"
                    placeholder="e.g., johndoe"
                    maxlength="12"
                    aria-label="Enter GitHub username"
                  />
                </div>
                <div class="col">
                  <label for="repo-org">Org</label>
                  <input
                    type="text"
                    name="org"
                    id="repo-org"
                    v-model="reposForm.org"
                    placeholder="e.g., github"
                    maxlength="12"
                    aria-label="Enter GitHub organization"
                  />
                </div>
              </div>
              <div class="col">
                <label for="repo-topic">Topic</label>
                <input
                  width="100%"
                  type="text"
                  name="topic"
                  id="repo-topic"
                  v-model="reposForm.topic"
                  placeholder="e.g., web,api"
                  maxlength="32"
                  aria-label="Enter comma-separated topics"
                />
              </div>
            </fieldset>

            <!-- Count -->
            <fieldset>
              <legend>Count</legend>
              <div class="grid">
                <div class="col">
                  <label for="min-size">Min Size (KB)</label>
                  <input
                    type="number"
                    name="min_size"
                    id="min-size"
                    v-model="reposForm.min_size"
                    placeholder="e.g., 500"
                    min="0"
                    step="1"
                    aria-label="Enter minimum repository size in KB"
                  />
                </div>
                <div class="col">
                  <label for="max-size">Max Size (KB)</label>
                  <input
                    type="number"
                    name="max_size"
                    id="max-size"
                    v-model="reposForm.max_size"
                    placeholder="e.g., 500"
                    min="0"
                    step="1"
                    aria-label="Enter maximum repository size in KB"
                  />
                </div>
                <div class="col">
                  <label for="followers-count">Followers</label>
                  <input
                    type="number"
                    name="followers"
                    id="followers-count"
                    v-model="reposForm.followers"
                    placeholder="e.g., 1000"
                    min="0"
                    step="1"
                    aria-label="Enter minimum number of followers"
                  />
                </div>
                <div class="col">
                  <label for="min-forks">Min Forks</label>
                  <input
                    type="number"
                    name="min_forks"
                    id="min-forks"
                    v-model="reposForm.min_forks"
                    placeholder="e.g., 50"
                    min="0"
                    step="1"
                    aria-label="Enter minimum number of forks"
                  />
                </div>
                <div class="col">
                  <label for="max-forks">Max Forks</label>
                  <input
                    type="number"
                    name="max_forks"
                    id="max-forks"
                    v-model="reposForm.max_forks"
                    placeholder="e.g., 200"
                    min="0"
                    step="1"
                    aria-label="Enter maximum number of forks"
                  />
                </div>
                <div class="col">
                  <label for="min-stars">Min Stars</label>
                  <input
                    type="number"
                    name="min_stars"
                    id="min-stars"
                    v-model="reposForm.min_stars"
                    placeholder="e.g., 500"
                    min="0"
                    step="1"
                    aria-label="Enter minimum number of stars"
                  />
                </div>
                <div class="col">
                  <label for="max-stars">Max Stars</label>
                  <input
                    type="number"
                    name="max_stars"
                    id="max-stars"
                    v-model="reposForm.max_stars"
                    placeholder="e.g., 10000"
                    min="0"
                    step="1"
                    aria-label="Enter maximum number of stars"
                  />
                </div>
                <div class="col">
                  <label for="topics-count">Topics Count</label>
                  <input
                    type="number"
                    name="topics"
                    id="topics-count"
                    v-model="reposForm.topics"
                    placeholder="e.g., 3"
                    min="0"
                    step="1"
                    aria-label="Enter exact number of topics"
                  />
                </div>
                <div class="col">
                  <label for="good-first-issues">Good First Issues</label>
                  <input
                    type="number"
                    name="good_first_issues"
                    id="good-first-issues"
                    v-model="reposForm.good_first_issues"
                    placeholder="e.g., 5"
                    min="0"
                    step="1"
                    aria-label="Enter minimum number of good first issues"
                  />
                </div>
                <div class="col">
                  <label for="help-wanted-issues">Help Wanted Issues</label>
                  <input
                    type="number"
                    name="help_wanted_issues"
                    id="help-wanted-issues"
                    v-model="reposForm.help_wanted_issues"
                    placeholder="e.g., 10"
                    min="0"
                    step="1"
                    aria-label="Enter minimum number of help wanted issues"
                  />
                </div>
              </div>
            </fieldset>

            <!-- Options -->
            <fieldset>
              <legend>Options</legend>
              <div class="grid">
                <div class="col">
                  <label>Forked</label>
                  <div>
                    <input
                      type="radio"
                      name="fork"
                      id="fork-true"
                      value="true"
                      v-model="reposForm.fork"
                    />
                    <label for="fork-true">Include Forks</label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      name="fork"
                      id="fork-only"
                      value="only"
                      v-model="reposForm.fork"
                    />
                    <label for="fork-only">Only Forks</label>
                  </div>
                </div>
                <div class="col">
                  <label>Mirror</label>
                  <div>
                    <input
                      type="radio"
                      name="mirror"
                      id="mirror-true"
                      value="true"
                      v-model="reposForm.mirror"
                    />
                    <label for="mirror-true">True</label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      name="mirror"
                      id="mirror-false"
                      value="false"
                      v-model="reposForm.mirror"
                    />
                    <label for="mirror-false">False</label>
                  </div>
                </div>
                <div class="col">
                  <label>Template</label>
                  <div>
                    <input
                      type="radio"
                      name="template"
                      id="template-true"
                      value="true"
                      v-model="reposForm.template"
                    />
                    <label for="template-true">True</label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      name="template"
                      id="template-false"
                      value="false"
                      v-model="reposForm.template"
                    />
                    <label for="template-false">False</label>
                  </div>
                </div>
                <div class="col">
                  <label>Archived</label>
                  <div>
                    <input
                      type="radio"
                      name="archived"
                      id="archived-true"
                      value="true"
                      v-model="reposForm.archived"
                    />
                    <label for="archived-true">True</label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      name="archived"
                      id="archived-false"
                      value="false"
                      v-model="reposForm.archived"
                    />
                    <label for="archived-false">False</label>
                  </div>
                </div>
                <div class="col">
                  <label>Sponsorable</label>
                  <div>
                    <input
                      type="radio"
                      name="sponsorable"
                      id="sponsorable-true"
                      value="true"
                      v-model="reposForm.sponsorable"
                    />
                    <label for="sponsorable-true">True</label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      name="sponsorable"
                      id="sponsorable-false"
                      value="false"
                      v-model="reposForm.sponsorable"
                    />
                    <label for="sponsorable-false">False</label>
                  </div>
                </div>
                <div class="col">
                  <label>Funding</label>
                  <div>
                    <input
                      type="radio"
                      name="funding"
                      id="funding-true"
                      value="true"
                      v-model="reposForm.funding"
                    />
                    <label for="funding-true">True</label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      name="funding"
                      id="funding-false"
                      value="false"
                      v-model="reposForm.funding"
                    />
                    <label for="funding-false">False</label>
                  </div>
                </div>
              </div>
              <div class="col">
                <label for="">License</label>
                <select name="license" id="license" v-model="reposForm.license">
                  <option
                    v-for="license in licenses"
                    :key="license.keyword"
                    :value="license.keyword"
                  >
                    {{ license.name }}
                  </option>
                </select>
              </div>
            </fieldset>

            <!-- Misc. -->
            <fieldset>
              <legend>Misc.</legend>
              <div class="grid">
                <div class="col">
                  <label for="order">Order</label>
                  <select name="order" id="order" v-model="reposForm.order">
                    <option value="stars">Stars</option>
                    <option value="forks">Forks</option>
                    <option value="updated">Updated</option>
                  </select>
                </div>
                <div class="col">
                  <label for="sort">Sort</label>
                  <select name="sort" id="sort" v-model="reposForm.sort">
                    <option value="asc">Ascending</option>
                    <option value="desc">Descending</option>
                  </select>
                </div>
              </div>
            </fieldset>
            <button class="button" type="submit">Submit</button>
          </form>
        </div>
      </div>
    </section>
  </div>

  <section>
    <Footer />
  </section>
</template>

<style scoped>
.section {
  min-height: 100dvh;
  height: fit-content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  padding: 2.5rem 0;
}
.heading {
  font-size: 3rem;
  letter-spacing: -4px;
  line-height: 1;
  margin-bottom: 1rem;
}
.diffSection {
  width: 100%;
  min-height: 100dvh;
  height: fit-content;
  background-color: hsla(160, 100%, 37%, 0.2);
  border: 2px solid hsla(160, 100%, 37%, 0.2);
  border-radius: 5px;
  padding: 2rem;
  gap: 2rem;
  font-size: 1.5rem;
  letter-spacing: -1px;
}
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  align-items: center;
}
.col {
  display: flex;
  flex-direction: column;
}
.col > div > label {
  margin-left: 1rem;
}
fieldset {
  border-radius: 5px;
  border-color: var(--color-title);
}
legend {
  font-size: 1.5em;
  font-weight: bold;
  letter-spacing: -1px;
  color: var(--color-title);
  padding: 0 0.2rem;
  border-radius: 4px;
}
input,
select {
  padding: 0.3rem;
  font-size: 1rem;
  border-radius: 5px;
  border: 1px solid var(--color-title);
  background-color: #18392d;
  color: var(--color-title);
}
select {
  width: 100%;
}
input:focus-visible {
  outline: var(--color-title) auto 1px;
}
select:focus-visible {
  outline: var(--color-title) auto 1px;
}
.button {
  width: 100%;
  margin-top: 1rem;
  padding: 0.7rem;
  font-size: 1.2rem;
  background-color: #18392d;
  border: 1.5px solid var(--color-title);
  border-radius: 5px;
  color: var(--color-title);
  transition: all 0.3s ease;
}
.button:hover {
  background-color: var(--color-title);
  color: #18392d;
  cursor: pointer;
}

@media (max-width: 768px) {
  .heading {
    font-size: 2.5rem;
    letter-spacing: -3px;
  }
  .diffSection {
    font-size: 1.2rem;
  }
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 620px) {
  .heading {
    font-size: 2rem;
  }
  .diffSection {
    font-size: 1rem;
    padding: 1rem;
  }
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
