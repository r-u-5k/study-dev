package hellojpa;

import jakarta.persistence.*;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor

@Entity
//@Table(name = "USER")
public class Member {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "member_id")
    private Long id;

    @Column(name = "username")
    private String username;

//    @Column(name = "team_id")
//    private Long teamId;

    @ManyToOne
    @JoinColumn(name = "team_id")
    private Team team;

    public void setTeam(Team team) {
        this.team = team;
        team.getMembers().add(this);
    }
}
