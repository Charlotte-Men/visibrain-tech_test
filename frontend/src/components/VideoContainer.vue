<template>
  <GameForm @videos-found="fetchVideos" />
  <div class="videos-list">
    <VideoInfos v-for="video in videos" :key="video.id" :video="video" />
  </div>
</template>

<script>
import { ref } from "vue";
import GameForm from "./GameForm.vue";
import VideoInfos from "./VideoInfos.vue";
import { fetchVideosByGame } from "../services/api";

export default {
  components: { GameForm, VideoInfos },
  setup() {
    const videos = ref([]);

    const fetchVideos = async (gameName) => {
      const result = await fetchVideosByGame(gameName);
      if (result.Videos) {
        videos.value = result.Videos;
      }
    };
    return { videos, fetchVideos };
  },
};
</script>
