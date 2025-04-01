<template>
  <form onsubmit="return false">
    <p>Enter a game name to see last Twitch videos about it:</p>
    <div>
      <input 
        v-model="gameName" 
        @keyup.enter="searchVideos" 
        placeholder="Game name"
      />
      <button @click="searchVideos">Search</button>
    </div>
  </form>
</template>

<script>
import { fetchVideosByGame } from "../services/api";
import { ref } from "vue";

export default {
  setup() {
    const gameName = ref("");

    async function searchVideos() {
      if (gameName.value.trim()) {
        const result = await fetchVideosByGame(gameName.value.trim())
        result && console.log(result)
      }
    };

    return { gameName, searchVideos };
  },
};
</script>
