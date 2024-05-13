package hellojpa;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
//@Table(name = "USER")
public class Member {
    @Id
    private Long id;
//    @Column(name = "username")
    private String name;

}
